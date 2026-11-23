.headers on
.mode column

-- Task 5: Leeds Eats task sheet
-- open with: sqlite3 leeds_eats.db   then   .read task.sql

-------- Bronze: warm up --------

-- 1. all columns for all drivers
SELECT * FROM drivers;

-- 2. name and price of Bangkok Garden dishes (restaurant 3)
SELECT name, price FROM menu_items
WHERE restaurant_id = 3;

-- 3. name of the Indian restaurants
SELECT name FROM restaurants
WHERE cuisine = 'Indian';

-- 4. how many customers
SELECT COUNT(*) AS number_of_customers FROM customers;

-------- Silver: requests --------

-- 5. vegetarian and price 8 or less, cheapest first
SELECT name, price, restaurant_id FROM menu_items
WHERE is_vegetarian = 1 AND price <= 8
ORDER BY price ASC;

-- 6. hygiene rating lower than 4, worst first
SELECT name, cuisine, hygiene_rating FROM restaurants
WHERE hygiene_rating < 4
ORDER BY hygiene_rating ASC;

-- 7. restaurants in LS6, best rating first
-- the rating is in reviews table, so I join orders and reviews to get it
SELECT r.name, r.postcode,
       ROUND(AVG(v.rating), 2) AS average_rating,
       COUNT(v.review_id) AS number_of_reviews
FROM restaurants r
JOIN orders o ON o.restaurant_id = r.restaurant_id
JOIN reviews v ON v.order_id = o.order_id
WHERE r.postcode LIKE 'LS6%'
GROUP BY r.restaurant_id, r.name, r.postcode
ORDER BY average_rating DESC;

-- 7 answer: same postcode is not same near.
-- LS6 is a big area, two restaurants in LS6 can be far away from each other.
-- The postcode here is only the restaurant address, not the delivery area,
-- and a restaurant outside LS6 can be nearer to the student.
-- Also we have no distance column, so this data cannot measure distance.

-- 8. University of Leeds email, newest first
SELECT name, email, joined_date FROM customers
WHERE email LIKE '%@leeds.ac.uk'
ORDER BY joined_date DESC;

-- 8 answer: I think no.
-- The email is only for university, the customer did not say yes to advertise.
-- It is also personal data, so we should only send to customer who agree.

-- 9. 10 newest cancelled orders
SELECT order_id, customer_id, restaurant_id, order_time FROM orders
WHERE status = 'cancelled'
ORDER BY order_time DESC
LIMIT 10;

-- 10a. vegetarian dishes of Pasta Pronto
SELECT name, price FROM menu_items
WHERE restaurant_id = 4 AND is_vegetarian = 1
ORDER BY price ASC;

-- 10b. most expensive dish of Pasta Pronto
SELECT name, price FROM menu_items
WHERE restaurant_id = 4
ORDER BY price DESC
LIMIT 1;

-------- Gold: think it through --------

-- 11. orders in October still 'placed'
SELECT order_id, customer_id, restaurant_id, driver_id, order_time, status
FROM orders
WHERE status = 'placed' AND order_time LIKE '2026-10%'
ORDER BY order_time ASC;

-- 11 why I choose these columns:
-- order_id      - the agent can find the order and tell the customer the number
-- customer_id   - to call the customer
-- restaurant_id - to ask the restaurant if the food is made
-- driver_id     - to see if any driver take the order. Here it is NULL, so no driver took it
-- order_time    - to see how long the order is stuck
-- status        - to check it is still 'placed'
-- delivery_fee is not useful for this problem, so I do not show it.

-- 12 why the two queries are wrong:
-- first one: error, because WHERE cannot be after LIMIT.
--   the order must be SELECT, FROM, WHERE, ORDER BY, LIMIT
-- second one: it can run but the answer is wrong, because there is no ORDER BY,
--   so it gives the first 5 rows in the table, not the 5 cheapest.
-- correct one:
SELECT name, price FROM menu_items
WHERE is_vegetarian = 1
ORDER BY price ASC
LIMIT 5;

-- 13. cheapest item
SELECT name, price FROM menu_items
ORDER BY price ASC
LIMIT 1;

-- 13 again with LIMIT 5
SELECT name, price FROM menu_items
ORDER BY price ASC
LIMIT 5;

-- 13 answer: with LIMIT 5 I get five different dishes and all of them cost 3.50,
-- so the cheapest is not only one dish, many dishes have the same cheapest price.
-- So if I take the first row, it is random.
-- Leeds Eats should tell the customer there are many dishes with the same lowest price,
-- and maybe order them by the restaurant rating.

-- 14. orders at 21:00 or later
SELECT COUNT(*) AS late_orders,
       (SELECT COUNT(*) FROM orders) AS total_orders
FROM orders
WHERE CAST(strftime('%H', order_time) AS INTEGER) >= 21;

-- 14 answer: 178 of 1300 is about 14%, so some people order late.
-- But this is not enough to start a new menu. We do not know if these orders
-- are delivered or cancelled, which restaurant is popular, how much money they pay,
-- or if customer really ask for late night food. We also need to know if the
-- restaurant is open at that time and if it is worth to pay driver so late.

-- 15. my own question
-- marketing team ask: "which cuisine has the best review? we want to show it on home page"
SELECT r.cuisine,
       ROUND(AVG(v.rating), 2) AS average_rating,
       COUNT(v.review_id) AS number_of_reviews
FROM restaurants r
JOIN orders o ON o.restaurant_id = r.restaurant_id
JOIN reviews v ON v.order_id = o.order_id
GROUP BY r.cuisine
ORDER BY average_rating DESC;
