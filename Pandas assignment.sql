CREATE DATABASE IF NOT EXISTS sql_translate;
USE sql_translate;

CREATE TABLE IF NOT EXISTS employees (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DepartmentID INT,
    Salary DECIMAL(10, 2),
    HireDate DATE,
    JobTitle VARCHAR(100)
);

select * from employees;

SELECT employee_id, first_name, last_name FROM employees WHERE department_id
= 10;

SELECT AVG(salary) as avg_salary, MAX(salary) as max_salary FROM employees
WHERE department_id = 20;

SELECT department_id, COUNT(employee_id) as num_employees FROM employees
GROUP BY department_id;

SELECT * FROM orders WHERE OrderDate >= '2022-01-01' AND CustomerID =
1;

INSERT INTO employees (FirstName, LastName, DepartmentID, Salary, HireDate, JobTitle)
VALUES
    ('John', 'Doe', 0001, 60000.00, '2022-01-01', 'Manager'),
    ('Jane', 'Smith', 0002, 55000.00, '2023-01-15', 'Engineer'),
    ('Tom', 'Sally', 0003, 75000.00, '2023-02-15', 'Director'),
    ('Ikol', 'Bnuy', 0004, 45000.00, '2023-03-15', 'Director'),
    ('Dash', 'Yikk', 0005, 35000.00, '2023-04-15', 'Intern'),
    ('Treii', 'Popp', 0006, 15000.00, '2023-04-15', 'Intern'),
    ('Asws', 'Juik', 0007, 12000.00, '2023-06-15', 'Intern'),
    ('Weres', 'Kliny', 0008, 34000.00, '2023-07-15', 'Manager'),
    ('Uimdf', 'Buysoye',0009, 35000.00, '2023-08-15', 'Manager'),
    ('Rvskiw', 'Acdow', 0010, 90000.00, '2023-08-15', 'Manager');
    
    update employees
    set DepartmentID = 22002
    where EmployeeID = 10;


CREATE TABLE IF NOT EXISTS orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    OrderAmount DECIMAL(10, 2)
);


INSERT INTO orders (CustomerID, OrderDate, OrderAmount)
VALUES
    (1, '2023-01-11', 1000.00),
    (2, '2023-01-22', 1500.00),
    (3, '2023-01-10', 3500.00),
    (3, '2023-02-01', 6500.00),
    (4, '2023-03-19', 8500.00),
    (4, '2023-03-17', 9500.00),
    (5, '2023-03-16', 9900.00),
    (5, '2023-03-14', 15000.00),
    (6, '2023-04-17', 15000.00),
    (6, '2023-04-19', 15100.00);