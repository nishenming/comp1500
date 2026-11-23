-- Week 1.9, Session 2, Task 5: make a small bank database
-- open with: sqlite3 branches.db   then   .read schema.sql

.headers on
.mode column

-- this line is needed, or the foreign key in Staff will not work
PRAGMA foreign_keys = ON;

-------- Task 1: Branch table --------
CREATE TABLE Branch (
    branch_id INTEGER PRIMARY KEY,
    street    TEXT NOT NULL,
    city      TEXT NOT NULL,
    postcode  TEXT NOT NULL
);

INSERT INTO Branch (branch_id, street, city, postcode) VALUES
    (1, 'Shaw Lane', 'Leeds', 'LS6 5UL');

SELECT * FROM Branch;

-------- Task 2: Staff table --------
CREATE TABLE Staff (
    staff_id INTEGER PRIMARY KEY,
    name     TEXT NOT NULL,
    role     TEXT CHECK (role IN ('Manager', 'Cashier')),
    branch   INTEGER,
    FOREIGN KEY (branch) REFERENCES Branch (branch_id)
);

-- role and branch are NULL, because the staff is not allocated yet
INSERT INTO Staff (staff_id, name, role, branch) VALUES
    (101, 'Tom', NULL, NULL);

SELECT * FROM Staff;

-------- Task 3: give a role and a branch --------
UPDATE Staff SET role = 'Manager' WHERE staff_id = 101;
UPDATE Staff SET branch = 1        WHERE staff_id = 101;

SELECT * FROM Staff;

-------- Task 4: add more data --------
INSERT INTO Branch (branch_id, street, city, postcode) VALUES
    (2, 'Kirkstall Road', 'Leeds', 'LS3 1LY');

INSERT INTO Staff (staff_id, name, role, branch) VALUES
    (102, 'Aisha', 'Cashier', 1),
    (103, 'Ben',   'Manager', 2),
    (104, 'Chloe', 'Cashier', 2);

SELECT * FROM Branch;
SELECT * FROM Staff;

-- test bad data. these two lines should give error.
-- first one: the same branch_id again
INSERT INTO Branch (branch_id, street, city, postcode) VALUES
    (1, 'Another Street', 'Leeds', 'LS1 1AA');
-- error: UNIQUE constraint failed: Branch.branch_id
-- because branch_id is PRIMARY KEY, so two rows cannot have the same id

-- second one: city is NULL
INSERT INTO Branch (branch_id, street, city, postcode) VALUES
    (3, 'Third Street', NULL, 'LS2 2BB');
-- error: NOT NULL constraint failed: Branch.city
-- because I write NOT NULL for city, so empty city is not allowed

-- these two rules protect the data. Without them the bad data will go in
-- and the table will be wrong.

-------- Task 5: simple queries --------
-- all the managers
SELECT staff_id, name, branch FROM Staff
WHERE role = 'Manager';

-- all the staff in one branch
SELECT staff_id, name, role FROM Staff
WHERE branch = 1;
