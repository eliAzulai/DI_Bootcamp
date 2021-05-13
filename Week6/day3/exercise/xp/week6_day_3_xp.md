Exercise 1: DVD Rental
Instructions
Get a list of all film languages.

SELECT * FROM LANGUAGE


Get a list of all films joined with their languages – select the following details : film title, description, and language name. Try your query with different joins:


SELECT film.title, film.description, language.name, language.language_id
FROM film
INNER JOIN language
ON film.film_id = language.language_id

Get all films, even if they don’t have languages.

SELECT film.title, film.description, language.name
FROM film
FULL OUTER JOIN language
ON film.film_id = language.language_id


Get all languages, even if there are no films in those languages.

SELECT * FROM language


Create a new table called new_film with the following columns : id, name. Add some new films to the table.

CREATE TABLE new_film (
id SERIAL PRIMARY KEY,
name VARCHAR (50) NOT NULL
); 

INSERT INTO new_film (name)
VALUES ('Harry Potter'),('Withnail and I'),('Jujitsu Kaisan')



Create a new table called customer_review, which will contain film reviews that customers will make.

Think about the DELETE constraint: if a film is deleted, it’s review should be automatically deleted.

It should have the following columns:
review_id – a primary key, non null, auto-increment.
film_id – references the new_film table. The film that is being reviewed.
language_id – references the language table. What language the review is in.
title – the title of the review.
score – the rating of the review (1-10).
review_text – the text of the review. No limit on the length.
last_update – when the review was last updated.

CREATE TABLE customer_review (
review_id SERIAL PRIMARY KEY,
flim_id INT references new_film (id) ON DELETE CASCADE,
language_id INT references language(language_id), 
title VARCHAR (50) NOT NULL,
socre INT,
reveiw_text TEXT,
last_update DATE)


Add 2 movie reviews. Make sure you link them to valid objects in the other tables.


INSERT INTO customer_review (flim_id, language_id, title, socre, reveiw_text, last_update)
VALUES ('1', '1', 'Is Harry Potter Worth The Hype', 7, 'bajlajjldskfjlasdfjasdlfj', '2021-05-11')
VALUES ('2', '3', 'Has Withnail Lost It ', 8, 'eryretyretysdlfj', '2021-05-4')


Delete a film that has a review from the new_film table, what happens to the customer_review table?

DELETE FROM customer_review WHERE title = 'Has Withnail Lost It ';


Exercise 2 : DVD Rental
Instructions
Use UPDATE to change the language of some films. Make sure that you use valid languages.

UPDATE film
SET language_id = 2
WHERE title = 'Chamber Italian'

UPDATE film
SET language_id = 3
WHERE title = 'Bright Encounters'

Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?

customer_id and store_id
we would provide the valid references for the shared information.



We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?

it was droped but not perhaps would remove references to other tables for the same entry. ie film if it is cascade. 


Find out how many rentals are still outstanding (ie. have not been returned to the store yet).

SELECT count(*) FROM rental WHERE return_date is NULL



Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)

SELECT rental.rental_id, film.title, film.rental_rate
FROM inventory
INNER JOIN rental
ON inventory.inventory_id = rental.inventory_id
INNER JOIN film
ON film.film_id = inventory.film_id
WHERE return_date IS NULL
ORDER BY rental_rate DESC 
LIMIT 30


Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?
The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.

SELECT film.title, film.description, actor.first_name
FROM film
INNER JOIN actor 
ON film.film_id = actor.actor_id
WHERE film.title LIKE '%sumo wrestler%' OR film.description LIKE '%sumo wrestler%' OR actor.first_name LIKE 'Penelope' AND actor.last_name = 'Monroe'


The 2nd film : A short documentary (less than 1 hour long), rated “R”.

SELECT * 
FROM film
WHERE rating = 'R' AND description LIKE '%Documentary%' AND length < 61


The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.

SELECT film.title, customer.first_name, customer.last_name, rental.return_date, payment.amount
FROM film
FULL OUTER JOIN customer
ON film.film_id = customer.customer_id
FULL OUTER JOIN payment
ON payment.payment_id = film.film_id
FULL OUTER JOIN rental
ON rental.rental_id = film.film_id
WHERE customer.first_name = 'Matthew' AND customer.last_name = 'Mahan' payment.amount > 4 


The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.

SELECT * 
FROM film
WHERE description LIKE '%boat%' OR title LIKE '%boat%' 
ORDER BY replacement_cost DESC

