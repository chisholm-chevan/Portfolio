import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='Generalboy$1', database='banking_system')

cursor = mydb.cursor()

cursor.execute('SELECT * FROM customer')
results = cursor.fetchall()
for row in results:
    print(row)


create_table_query = """
CREATE TABLE IF NOT EXISTS user_email (
id INT AUTO_INCREMENT PRIMARY KEY, 
username varchar(255), 
email varchar(255)
)
"""
cursor.execute(create_table_query)

insert_data_query = """
INSERT INTO user_email (username, email) VALUES (%s, %s)
"""
user_data = [("Alice123", "alicewonderkid@gmail.com"), ("BobXavier", "Bobbylolly22@gmail.com")]

cursor.executemany(insert_data_query, user_data)
mydb.commit()


update_query = """
#UPDATE user_email SET email = %s WHERE username = %s
"""
new_email = "aliceinwonderland343@gmail.com"
user_to_update = "Alice123"

cursor.execute(update_query, (new_email, user_to_update))
mydb.commit()

cursor.execute("SELECT * FROM user_email LIMIT 2")
print("\nData after update:")
for row in cursor.fetchall():
    print(row)

cursor.close()
mydb.close()