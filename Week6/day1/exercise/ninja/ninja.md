<!-- Exercise 1 : Bootcamp
<!--  -->
<!-- Continuation of the Exercise XPGold -->

<!-- Select -->
<!-- For the following questions, you have to fetch the first_names, last_names and birth_dates of the students. -->

<!-- Fetch the first four students. You have to order the four students alphabetically by last_name. -->

<!-- Fetch three students skipping the first two students. --> -->

SELECT first_name, last_name, birth_date FROM public.students ORDER BY birth_date ASC LIMIT 1;

<!-- Fetch the details of the youngest student. -->

SELECT first_name, last_name, birth_date FROM public.students ORDER BY birth_date ASC LIMIT 1;

<!-- Fetch three students skipping the first two students. --> -->

SELECT first_name, last_name, birth_date FROM public.students OFFSET 2;
