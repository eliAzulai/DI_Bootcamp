import psycopg2
# import psycopg2.extras


HOSTNAME = '127.0.0.1'
USERNAME = 'Azulai'
PASSWORD = 'password'
DATABASE = 'restaurant'


connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
# cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)


cursor = connection.cursor()
cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
query = "SELECT * FROM customer LIMIT 20;"

cursor.execute(query)

results = cursor.fetchall()

connection.close()

for item in results:
        print(item)


class MenuItem:
    def __init__ (self, name, price):
        name = name
        price = price 
         
    def all():
        
    def get_by_name():
    
    def save():
    
        
    def delete():
    
    
    def update():
    
    
    