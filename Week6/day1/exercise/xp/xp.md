INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Natalie','Portman','09/9/1981', 1);

SELECT * FROM actors
LIMIT 4;

CREATE TABLE items (
item_id SERIAL PRIMARY KEY,
product VARCHAR (50) NOT NULL,
price SMALLINT NOT NULL);


CREATE TABLE customers (
customer_id SERIAL PRIMARY KEY,
first_name VARCHAR (50) NOT NULL,
last_name VARCHAR (50) NOT NULL);

INSERT INTO items (product, price)
VALUES ('Small_desk', 100),
('Large_desk', 300),
('Fan', 80);

INSERT INTO customers (first_name, last_name)
VALUES ('Greg','Jones'),
('Sandra', 'Jones'),
('Scott', 'Scott'),
('Trevor', 'Green'),
('Melanie', 'Johnson');

SELECT * FROM public.items

SELECT * FROM public.items WHERE price > 80;

SELECT * FROM public.items WHERE price <= 300;

SELECT * FROM public.customers WHERE last_name = 'Smith';

SELECT * FROM public.customers WHERE last_name = 'Jones';

SELECT * FROM public.customers WHERE first_name != 'Scott';