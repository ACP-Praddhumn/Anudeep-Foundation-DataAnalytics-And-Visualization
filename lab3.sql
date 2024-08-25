-- lab_assignment1.sql

-- Creating the BankAccount table with account_id, account_holder_name, and account_balance columns
CREATE TABLE BankAccount (
    account_id INT PRIMARY KEY,
    account_holder_name VARCHAR(100),
    account_balance DECIMAL(10, 2)
);
-- Task 1: Insert Data
-- Inserting data into the BankAccount table
INSERT INTO BankAccount (account_id, account_holder_name, account_balance)
VALUES (101, 'John Doe', 45000);
INSERT INTO BankAccount (account_id, account_holder_name, account_balance)
VALUES (102, 'Jane Smith', 32000);
INSERT INTO BankAccount (account_id, account_holder_name, account_balance)
VALUES (103, 'Mike Johnson', 28000);
INSERT INTO BankAccount (account_id, account_holder_name, account_balance)
VALUES (104, 'Emily Davis', 50000);
INSERT INTO BankAccount (account_id, account_holder_name, account_balance)
VALUES (105, 'Sarah Wilson', 15000);

-- Task 2: Retrieving Data
-- Retrieving the account_holder_name and account_balance of all account holders
SELECT account_holder_name, account_balance 
FROM BankAccount;

-- Task 3: Filtering Data
-- Retrieving the account_holder_name and account_balance where the account_balance is more than 30,000
SELECT account_holder_name, account_balance 
FROM BankAccount
WHERE account_balance > 30000;

-- Task 4: Updating Data
-- Updating the account_balance of the account holder whose ID is 101
UPDATE BankAccount
SET account_balance = 47000
WHERE account_id = 101;



-- Task 4: Retrieve and display information about students from the student table 
-- in ascending order based on their last names.

-- SELECT query to retrieve all columns from the student table
-- and display the results in ascending order of the last names.
SELECT * 
FROM student
ORDER BY last_name ASC;


-- Task  5: Count the number of students based on their gender
-- from the student table.

-- SELECT query to count the number of students for each gender
-- and group the results by gender.
SELECT gender, COUNT(*) AS student_count
FROM student
GROUP BY gender;


-- Task 6: Add two new columns to the Employee table named Salary and Department.
ALTER TABLE Employee
ADD COLUMN Salary DECIMAL(10, 2),
ADD COLUMN Department VARCHAR(50);

-- Task 7: Insert data into the Employee table with the new columns.
INSERT INTO Employee (emp_id, name, manager_id, Salary, Department)
VALUES 
(1, 'John Doe', 2, 60000, 'IT'),
(2, 'Jane Smith', NULL, 75000, 'HR'),
(3, 'Emily Johnson', 2, 45000, 'Finance'),
(4, 'Michael Brown', 1, 52000, 'IT'),
(5, 'Emma Davis', 1, 48000, 'Marketing');

-- Task 8: Retrieve all employees from the Employee table 
-- who have a salary greater than 50000 and are in the 'IT' department.
SELECT * FROM Employee
WHERE Salary > 50000 AND Department = 'IT';


-- Task 8: Find products from the "product" table that are either in the 'Electronics' category 
-- or have a price less than 70000.

SELECT * 
FROM product
WHERE category = 'Electronics' 
   OR price < 70000;


-- Task 9: Calculate the average salary of employees in each department

-- Query to calculate the average salary of employees in each department
SELECT department, AVG(Salary) AS average_salary
FROM employee
GROUP BY department;