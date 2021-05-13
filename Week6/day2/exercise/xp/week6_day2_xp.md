Exercise 1 : Items And Customers
Instructions
We will work on the public database that we created yesterday.

Use SQL to get the following from the database:
All items, ordered by price (lowest to highest).

SELECT * FROM items ORDER BY price ASC;

Items with a price above 80 (80 included), ordered by price (highest to lowest).

SELECT * FROM items WHERE price > 80 
ORDER BY price DESC;

The first 3 customers in alphabetical order (A-Z) – exclude ‘id’ from the results.
All last names (no other columns!), in reverse alphabetical order (Z-A)

select last_name from customers order by last_name asc
limit 3; 

Create a table named purchases. It should have 2 columns : customer_id and item_id. These columns are references from the tables customers and items. Edit the data of the purchases table:


CREATE TABLE purchases(
purchases_id SERIAL,
customer_id INTEGER, 
item_id INTEGER,
PRIMARY KEY (purchases_id),
FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
FOREIGN KEY (item_id) REFERENCES items(item_id)
);

Add a row which references a customer by ID, but does not reference an item by ID (leave it blank). Does this work? Why/why not?

INSERT INTO purchases (customer_id, item_id)
VALUES (1,) 
it doesnt work becuase you need a reference. 


Add 5 rows which reference existing customers and items.

-- INSERT INTO purchases (customer_id, item_id)
-- VALUES(1, 2),(2,1),(3,3),(3,2),(4,2),(5,1);


Use SQL to get the following from the database:


All purchases. Is this information useful to us?

SELECT * FROM purchases



All purchases, joining with the customers table.

SELECT purchases.customer_id, purchases.item_id, customers.first_name, customers.last_name
FROM customers
INNER JOIN purchases
ON customers.customer_id = purchases.purchases_id;


Purchases of the customer with the ID equal to 4.
SELECT purchases.customer_id, purchases.item_id, customers.first_name, customers.last_name
FROM customers
INNER JOIN purchases
ON customers.customer_id = purchases.purchases_id
WHERE customers.customer_id = 4;

Purchases for a large desk AND a small desk

SELECT purchases.customer_id, purchases.item_id, customers.first_name, customers.last_name
FROM customers
INNER JOIN purchases
ON customers.customer_id = purchases.purchases_id
WHERE purchases.item_id = 1 OR purchases.item_id =2;


Create a purchase for Scott Scott – he bought a hard drive.
INSERT INTO items (product, price)
VALUES ('hard drive', '200')

INSERT INTO purchases (customer_id, item_id)
VALUES (3,4)



Use SQL to show all the customers who have made a purchase. Show the following fields/columns:
Customer first name
Customer last name
Item name


SELECT purchases.item_id, customers.first_name, customers.last_name, items.product
FROM customers
INNER JOIN purchases
ON customers.customer_id = purchases.purchases_id
INNER JOIN items ON customers.customer_id = items.item_id;



Exercise 2 : Dvdrental Database

<!-- 

We will use the newly installed dvdrental database.

In the dvdrental database write a query to select all the columns from the “customer” table.

SELECT * FROM customer


Write a query to display the names (first_name, last_name) using an alias named “full_name”.

SELECT first_name AS full_name, last_name AS full_name FROM customer


Lets get all the dates that accounts were created. Write a query to select all the create_date from the “customer” table (there should be no duplicates).

SELECT DISTINCT create_date FROM customer


Write a query to get all the customer details from the customer table, it should be displayed in descending order by their first name.

SELECT * FROM customer ORDER BY first_name DESC;


Write a query to get the film ID, title, description, year of release and rental rate in ascending order according to their rental rate.

SELECT film_id, title, description, release_year, rental_rate 
FROM film
ORDER BY rental_rate ASC



Write a query to get the address, and the phone number of all customers living in the Texas district, these details can be found in the “address” table.

SELECT address, phone, district
FROM address
WHERE district = 'Texas'



Write a query to retrieve all movie details where the movie id is either 15 or 150.

SELECT * 
FROM film
WHERE film_id = 15 OR film_id = 150


Write a query which should check if your favorite movie exists in the database. Have your query get the film ID, title, description, length and the rental rate, these details can be found in the “film” table.


SELECT film_id, title, description, length, rental_rate 
FROM film
WHERE title = 'The Italian Job'


No luck finding your movie? Maybe you made a mistake spelling the name. Write a query to get the film ID, title, description, length and the rental rate of all the movies starting with the two first letters of your favorite movie.


SELECT film_id, title, description, length, rental_rate 
FROM film
WHERE title LIKE 'Th%'



Write a query which will find the 10 cheapest movies.

SELECT film_id, title, replacement_cost
FROM film
ORDER BY replacement_cost ASC 
LIMIT 10


Not satisfied with the results. Write a query which will find the next 10 cheapest movies.
Bonus: Try to not use LIMIT.


SELECT film_id, title, replacement_cost
FROM film
ORDER BY replacement_cost ASC 
LIMIT 10 OFFSET 10


Write a query which will join the data in the customer table and the payment table. You want to get the amount and the date of every payment made by a customer, ordered by their id (from 1 to…).


SELECT customer.customer_id, payment.amount, payment.payment_date
FROM customer 
FULL OUTER JOIN payment
ON customer.customer_id = payment_id
ORDER BY customer.customer_id

You need to check your inventory. Write a query to get all the movies which are not in inventory.

SELECT inventory.inventory_id, rental.return_date,rental.rental_id
FROM inventory
FULL OUTER JOIN rental
ON inventory.inventory_id = rental.rental_id
WHERE rental.return_date IS NULL OR inventory.inventory_id IS NULL

Write a query to find which city is in which country.


SELECT city.city, country.country
FROM city 
INNER JOIN country  
ON city.city_id = country.country_id 



Bonus You want to be able to see how your sellers have been doing? Write a query to get the customer’s id, names (first and last), the amount and the date of payment ordered by the id of the staff member who sold them the dvd. -->



