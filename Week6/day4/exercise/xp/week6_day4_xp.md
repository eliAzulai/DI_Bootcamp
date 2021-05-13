Basic Select Statement
Write a query to display the names (first_name, last_name) using an alias name “First Name”, “Last Name” from the employee table.

SELECT first_name AS "First Name", last_name AS "Last Name"
FROM employees



Write a query to get unique departments ID from the employee table (ie. without duplicates).



SELECT DISTINCT department_id FROM employees


Write a query to get the details of all employees from the employee table, do so in descending order by first name.

SELECT * FROM employees
ORDER BY first_name desc


Write a query to get the names (first_name, last_name), salary and 15% of salary as PF (ie. alias) for all the employees.

didnt understand what that meant

SELECT first_name, last_name, salary AS "15%"
FROM employees



Write a query to get the employee IDs, names (first_name, last_name) and salary in ascending order according to their salary.

SELECT employee_id, first_name, last_name, salary
FROM employees
ORDER BY salary asc



Write a query to get the total sum of all salaries paid to the employees.


SELECT SUM (salary)
FROM employees


Write a query to get the maximum and minimum salaries paid to the employees.

SELECT MIN (salary), MAX (salary)
FROM employees


Write a query to get the average salary paid to the employees.

SELECT AVG (salary)
FROM employees

Write a query to get the number of employees working in the company.

SELECT COUNT (employee_id)
FROM employees

Write a query to get all the first names from the employees table in upper case

SELECT UPPER (first_name) 
FROM employees


Write a query to get the first three characters of each first name of all the employees in the employees table.

SELECT SUBSTRING (first_name, 1,3) 
FROM employees



Write a query to get the full names of all the employees in the employees table. You have to include the first name and last name.

SELECT concat (first_name, ' ', last_name) AS "FULL NAME"
FROM employees


Write a query to get the first name, last name and the length of the full name of all the employees from the employees table.


SELECT length(concat(first_name, ' ', last_name))
FROM employees

Write a query to check whether the first_name column of the employees table contains any numbers.


SELECT first_name 
FROM employees
WHERE first_name REGEXP '[0-9]'

Write a query to select the first ten records from a table.

SELECT *
FROM employees 
LIMIT 10





Restricting And Sorting
Write a query to display the first_name, last_name and salary of all employees whose salary is between $10,000 and $15,000.


SELECT first_name, last_name, salary 
FROM employees 
WHERE salary > 10000 AND salary < 15000



Write a query to display the first_name, last_name and hire date of all employees who were hired in 1987.


SELECT first_name, last_name, hire_date 
FROM employees 
WHERE hire_date BETWEEN '1987-01-01' AND '1988-01-31'


Write a query to get the all employees whose first_name has both the letters ‘c’ and ‘e’.

SELECT first_name
FROM employees 
WHERE first_name LIKE '%c%' AND first_name LIKE '%e%'

Write a query to display the last_name, job, and salary of all the employees who don’t work as Programmers or Shipping Clerks, and who don’t receive a salary equal to $4,500, $10,000, or $15,000.

SELECT *
FROM employees AS e
INNER JOIN jobs AS j
ON e.employee_id = j.job_id 
WHERE salary != 4000 OR salary != 10000 OR salary != 15000



Write a query to display the last names of all employees whose last name contains exactly six characters.

SELECT length(last_name) len
FROM employees
WHERE length(last_name)=6


Write a query to display the last name of all employees who have the letter ‘e’ as the third character in the name.


SELECT SUBSTRING (last_name,3,1) AS baba
FROM employees 
WHERE SUBSTRING (last_name,3,1) = 'e'

Write a query to display the jobs/designations available in the employees table.




Write a query to select all information of employees whose last name is either ‘JONES’ or ‘BLAKE’ or ‘SCOTT’ or ‘KING’ or ‘FORD’.

SELECT last_name
FROM employees
WHERE last_name = 'Jones' OR last_name = 'Blake' OR last_name = 'Scott' OR last_name = 'King' OR last_name = 'Ford'


