import sqlite3 as sl
from faker import Faker
from time import time
f = Faker()
connection = sl.connect("people.db")
cursor = connection.cursor()
start = time()
for i in range(2):
    query = f"INSERT INTO people (name, email) VALUES ('{f.email()}', '{f.name()}')"
    cursor.execute(query)
connection.commit()
connection.close()
end = time()
print(end - start)