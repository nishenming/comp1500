.headers on
.mode column

-- Task 5: Leeds Eats task sheet
-- Run with:  sqlite3 leeds_eats.db   then   .read task.sql

-----------------------------------------
-- Bronze: warm-up
-----------------------------------------

-- 1. every column for every driver
SELECT * FROM drivers;

-- 2. name and price of every dish from Bangkok Garden (restaurant 3)
SELECT name, price FROM menu_items
WHERE restaurant_id = 3;

-- 3. names of the Indian restaurants
SELECT name FROM restaurants
WHERE cuisine = 'Indian';

-- 4. how many customers
SELECT COUNT(*) AS number_of_customers FROM customers;

-----------------------------------------
-- Silver: requests from customers and staff
-----------------------------------------

-- 5. vegetarian, £8 or less, cheapest first
SELECT name, price, restaurant_id FROM menu_items
WHERE is_vegetarian = 1 AND price <= 8
ORDER BY price ASC;

-- 6. hygiene rating below 4, worst first
SELECT name, cuisine, hygiene_rating FROM restaurants
WHERE hygiene_rating < 4
ORDER BY hygiene_rating ASC;

-- 7. restaurants with an LS6 postcode, best rated first
-- 'rated' means the average review score, so we need orders and reviews as well
SELECT r.name, r.postcode,
       ROUND(AVG(v.rating), 2) AS average_rating,
       COUNT(v.review_id) AS number_of_reviews
FROM restaurants r
JOIN orders o ON o.restaurant_id = r.restaurant_id
JOIN reviews v ON v.order_id = o.order_id
WHERE r.postcode LIKE 'LS6%'
GROUP BY r.restaurant_id, r.name, r.postcode
ORDER BY average_rating DESC;

-- 7 (explanation)
-- A matching postcode does not really mean the restaurant is near.
-- A district such as LS6 covers a large area, so two LS6 restaurants can be
-- miles apart. The postcode stored here is the restaurant's registered
-- address, not its delivery area, and a restaurant just outside LS6 could be
-- closer to the student. There is also no distance column, so this data
-- cannot measure distance at all.

-- 8. University of Leeds addresses, newest first
SELECT name, email, joined_date FROM customers
WHERE email LIKE '%@leeds.ac.uk'
ORDER BY joined_date DESC;

-- 8 (should Leeds Eats send the email?)
-- No. Having a university email address does not mean the person agreed to
-- marketing. Under UK GDPR they would need a lawful basis, usually consent,
-- and a student's university address is personal data that should not be
-- reused for marketing just because it is in the database. The marketing team
-- should send only to customers who opted in.

-- 9. the 10 most recent cancelled orders
SELECT order_id, customer_id, restaurant_id, order_time FROM orders
WHERE status = 'cancelled'
ORDER BY order_time DESC
LIMIT 10;

-- 10a. which of Pasta Pronto's dishes are vegetarian
SELECT name, price FROM menu_items
WHERE restaurant_id = 4 AND is_vegetarian = 1
ORDER BY price ASC;

-- 10b. Pasta Pronto's most expensive dish
SELECT name, price FROM menu_items
WHERE restaurant_id = 4
ORDER BY price DESC
LIMIT 1;

-----------------------------------------
-- Gold: think it through
-----------------------------------------

-- 11. October orders that still say 'placed'
SELECT order_id, customer_id, restaurant_id, driver_id, order_time, status
FROM orders
WHERE status = 'placed' AND order_time LIKE '2026-10%'
ORDER BY order_time ASC;

-- 11 (why these columns)
-- order_id      - a reference the agent can look up and quote to the customer
-- customer_id   - so the customer can be contacted
-- restaurant_id - so the restaurant can be asked whether the food was made
-- driver_id     - to see whether a driver was ever assigned. For these rows it
--                 is NULL, so no driver picked the order up.
-- order_time    - to see how long it has been stuck
-- status        - to confirm it is still 'placed'
-- delivery_fee is not needed: it does not help anyone solve the problem.

-- 12 (what is wrong with the two queries)
-- (a) SELECT name, price FROM menu_items ORDER BY price LIMIT 5 WHERE is_vegetarian = 1;
--     Syntax error. The clauses must be in the order
--     SELECT ... FROM ... WHERE ... ORDER BY ... LIMIT ...
--     so WHERE cannot come after LIMIT.
-- (b) SELECT name, price FROM menu_items WHERE is_vegetarian = 1 LIMIT 5;
--     It runs, but there is no ORDER BY, so SQLite returns the first five
--     matching rows in storage order. That is not the five cheapest dishes,
--     it is just five vegetarian dishes.
-- Correct version:
SELECT name, price FROM menu_items
WHERE is_vegetarian = 1
ORDER BY price ASC
LIMIT 5;

-- 13. the cheapest thing on Leeds Eats
SELECT name, price FROM menu_items
ORDER BY price ASC
LIMIT 1;

-- 13 (same query with LIMIT 5)
SELECT name, price FROM menu_items
ORDER BY price ASC
LIMIT 5;

-- 13 (what I noticed)
-- With LIMIT 5 the answer is five different dishes that all cost £3.50, so
-- 'the cheapest thing' is a tie, not one item. Taking the first row is
-- arbitrary and depends on storage order. Leeds Eats should tell the
-- customer that several dishes cost the same lowest price, and could break
-- the tie using something the customer cares about, such as the highest
-- rated restaurant.

-- 14. orders placed at 21:00 or later
SELECT COUNT(*) AS late_orders,
       (SELECT COUNT(*) FROM orders) AS total_orders
FROM orders
WHERE CAST(strftime('%H', order_time) AS INTEGER) >= 21;

-- 14 (is it enough evidence?)
-- 178 out of 1300 orders is about 14%, so there is some late demand, but a
-- count alone will not justify a new menu. It does not say whether those
-- orders were delivered or cancelled, which restaurants and cuisines they
-- came from, how much they were worth, or whether customers actually asked
-- for late-night food. We would also want to know if restaurants are open at
-- that time and whether it is profitable to keep drivers working that late.

-- 15. my own question
-- Request from the marketing team:
--   "Which cuisine gets the best reviews? We want to feature it on the home page."
SELECT r.cuisine,
       ROUND(AVG(v.rating), 2) AS average_rating,
       COUNT(v.review_id) AS number_of_reviews
FROM restaurants r
JOIN orders o ON o.restaurant_id = r.restaurant_id
JOIN reviews v ON v.order_id = o.order_id
GROUP BY r.cuisine
ORDER BY average_rating DESC;
