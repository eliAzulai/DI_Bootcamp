CREATE TABLE students (
id SERIAL PRIMARY KEY,
last_name VARCHAR (50) NOT NULL,
first_name VARCHAR (50) NOT NULL, 
birth_date DATE NOT NULL);

INSERT students (first_name, last_name, birth_date)
VALUES
('Marc', 'Benichou', '02/11/1998'),
('Yoan'	'Cohen', '03/12/2010'),
('Lea', 'Benichou', '27/07/1987'),
('Amelia', 'Dux', '07/04/1996'),
('David', 'Grez', '14/06/2003'),
('Omer', 'Simpson', '03/10/1980');

<!-- select -->
<!-- Fetch all of the data from the table. -->
SELECT * FROM public.students;

<!-- Fetch all of the students first_names and last_names. -->
SELECT first_name, last_name FROM public.students;
<!-- Fetch the student which id is equal to 2. -->
SELECT first_name, last_name FROM public.students WHERE id = 2;
<!-- Fetch the student whose last_name is Benichou AND first_name is Marc. -->

SELECT first_name, last_name FROM public.students WHERE last_name = 'Benichou' and first_name = 'Marc';
<!-- Fetch the students whose last_name is Benichou OR first_name is Marc. -->

SELECT first_name, last_name FROM public.students WHERE last_name = 'Benichou' or first_name = 'Marc';
<!-- Fetch the students whose first_name contains the letter a. -->

SELECT first_name, last_name FROM public.students WHERE first_name LIKE '%a%';
<!-- Fetch the students whose first_name starts with the letter a. -->

SELECT first_name, last_name FROM public.students WHERE first_name ILIKE 'a%';
<!-- Fetch the students whose first_name ends with the letter a. -->

SELECT first_name, last_name FROM public.students WHERE first_name LIKE '%a';

<!-- Fetch the students whose second to last letter of their first_names is a (Example: Leah). -->

SELECT first_name, last_name FROM public.students WHERE POSITION ('a' IN first_name) = 3;

<!-- Fetch the students whose id’s are equal to 1 AND 3 . -->
SELECT first_name, last_name FROM public.students WHERE id = 1 or id = 3;

<!-- Fetch the students whose birth_dates are equal to or come after 1/01/2000. (show all their inf -->

SELECT * FROM public.students WHERE birth_date >= '2000-01-1';

