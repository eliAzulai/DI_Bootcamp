Instructions
Create 3 different tables, each one with a different relationship.
Join them with all the types of PostgreSQL Joins you’ve learned.


CREATE TABLE customers (
customer_id SERIAL PRIMARY KEY,
first_name VARCHAR,
last_name VARCHAR

INSERT INTO customers (first_name, last_name)
)

CREATE TABLE items (
item_id SERIAL PRIMARY KEY, 
product_name VARCHAR (100),

)

CREATE TABLE payment (
payment_id SERIAL PRIMARY KEY, 
customer_id INT,
FOREIGN KEY(customer_id) 
REFERENCES customers(customer_id)	
)
	
CREATE TABLE contacts (
contacts_id SERIAL PRIMARY KEY,
customer_id INT, 
email VARCHAR (100)
supplier_name VARCHAR ()
FOREIGN KEY (customer_id)
REFERENCES customers(customer_id)	
)