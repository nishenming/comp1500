-- Week 1.9, Session 2, Task 5: create and manage a small banking database
-- Run with:  sqlite3 branches.db   then   .read schema.sql

.headers on
.mode column

-- The foreign key in Staff is only enforced if this is switched on
PRAGMA foreign_keys = ON;

-----------------------------------------
-- Task 1 - Branch relation
-----------------------------------------
CREATE TABLE Branch (
    branch_id INTEGER PRIMARY KEY,
    street    TEXT NOT NULL,
    city      TEXT NOT NULL,
    postcode  TEXT NOT NULL
);

INSERT INTO Branch (branch_id, street, city, postcode) VALUES
    (1, 'Shaw Lane', 'Leeds', 'LS6 5UL');

SELECT * FROM Branch;

-----------------------------------------
-- Task 2 - Staff relation
-----------------------------------------
CREATE TABLE Staff (
    staff_id INTEGER PRIMARY KEY,
    name     TEXT NOT NULL,
    role     TEXT CHECK (role IN ('Manager', 'Cashier')),
    branch   INTEGER,
    FOREIGN KEY (branch) REFERENCES Branch (branch_id)
);

-- role and branch are NULL until the person is allocated to a job
INSERT INTO Staff (staff_id, name, role, branch) VALUES
    (101, 'Tom', NULL, NULL);

SELECT * FROM Staff;

-----------------------------------------
-- Task 3 - allocate a role and a branch
-----------------------------------------
UPDATE Staff SET role = 'Manager' WHERE staff_id = 101;
UPDATE Staff SET branch = 1        WHERE staff_id = 101;

SELECT * FROM Staff;

-----------------------------------------
-- Task 4 - add more data
-----------------------------------------
INSERT INTO Branch (branch_id, street, city, postcode) VALUES
    (2, 'Kirkstall Road', 'Leeds', 'LS3 1LY');

INSERT INTO Staff (staff_id, name, role, branch) VALUES
    (102, 'Aisha', 'Cashier', 1),
    (103, 'Ben',   'Manager', 2),
    (104, 'Chloe', 'Cashier', 2);

SELECT * FROM Branch;
SELECT * FROM Staff;

-- Testing the constraints. Both statements below are expected to fail.
-- (a) a repeated primary key
INSERT INTO Branch (branch_id, street, city, postcode) VALUES
    (1, 'Another Street', 'Leeds', 'LS1 1AA');
-- expected: UNIQUE constraint failed: Branch.branch_id
-- The PRIMARY KEY on branch_id stops a second branch with the same id.

-- (b) a NULL city
INSERT INTO Branch (branch_id, street, city, postcode) VALUES
    (3, 'Third Street', NULL, 'LS2 2BB');
-- expected: NOT NULL constraint failed: Branch.city
-- Because city was declared NOT NULL, the row is rejected.

-- The two constraints are what protect the data: without them both of these
-- bad rows would go in and the tables would become unreliable.

-----------------------------------------
-- Task 5 - simple queries
-----------------------------------------
-- all the managers
SELECT staff_id, name, branch FROM Staff
WHERE role = 'Manager';

-- all the staff at one branch
SELECT staff_id, name, role FROM Staff
WHERE branch = 1;
