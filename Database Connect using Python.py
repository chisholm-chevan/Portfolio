"""
Assignment Question 1: Database Connectivity using Python
Task 1: Database Connection
Write a Python script to connect to a MySQL database using the mysql-connector library.
The database details such as hostname, username, password, and database name should be configurable.
Task 2: Data Retrieval
a) Implement a function to execute a SELECT query to retrieve all records from a specified table.
b) Display the retrieved data in a readable format.
Task 3: Data Insertion
Implement a function to insert a new record into a specified table. The function should take user input for the values of each column.
Task 4: Error Handling
Include appropriate error handling mechanisms in your script. Handle common issues such as connection errors, query execution errors, etc. Display meaningful error messages to the user.
Task 5: Bonus
Implement an additional feature of your choice, such as updating existing records, deleting records, or any other functionality that demonstrates a good understanding of database connectivity in Python.
Note: Use the mysql-connector library for MySQL databases. You can install it using pip install mysql-connector-python.
"""
import mysql.connector  # - Importing the SQL library to create a connection with MSQL database
from mysql.connector import errorcode
try:
    # Database Connection
    mydb = mysql.connector.connect(host='localhost', user='root', password='Generalboy$1', database='assignment')
    cursor = mydb.cursor()  # - A cursor allows us to interact with the database through queries. Acts like a mouse/keyboard
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Access denied: Check your username and password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist.")
    else:
        print(f"MySQL Error: {err}")

def select_que():  # - A select query function to select all records from a specific table
    cursor.execute("SELECT * FROM Human_res")
    results = cursor.fetchall()
    for row in results:
        print(row)


def insert_que():  # - A insert query to insert data via user input into the database
    # Data Insertion
    global work_id, fname, lname, email, salary, insert_data_query, user_data
    print("How many employees do you want to enter into the database")
    x = int(input(": "))
    k = 0
    while k < x:
        work_id = int(input("May i have your work ID - Must be a 3 digit number starting with 1: "))
        fname = input("Please enter your first name: ")
        lname = input("Please enter your last name: ")
        email = input("Please enter your email address: ")
        salary = int(input("Please enter the amount you earn per month: "))
        print("Data inserted Sucessfully")
        k += 1
        insert_data_query = """
        INSERT INTO Human_res (work_id, First_name, Last_name, email, salary) VALUES (%s, %s, %s, %s, %s)
        """
        user_data = [(work_id, fname, lname, email, salary)]
        cursor.executemany(insert_data_query, user_data)
        mydb.commit()  # - This allows us to confirm the changes made via the queries on the database side of connection


def del_query():  # A delete query funtion to delete records from within the database table
    print("Please enter the ID number of the first employee you want to delete")
    y = int(input())
    print("Please enter the ID number of the second employee you want to delete")
    x = int(input())
    delete_data_query = "DELETE FROM Human_res WHERE work_id = %s and %s"
    cursor.execute(delete_data_query, (y, x))
    mydb.commit()
    print("Data Deleted Successfully")



def update_que():  # - An update query function to update records within a table whose data were already inserted
    print("Please enter the ID number of the employee you whose email you would like to update")
    x = input()
    print("Please enter the new email address")
    y = input()
    update_data_query = """ UPDATE Human_res SET email = %s WHERE work_id = %s"""
    cursor.execute(update_data_query,(y, x))
    mydb.commit()
    print("Data updated successfully")


# --------------------------------------MAIN PROGRAM----------------------------------------------
# create_table_query = """
# CREATE TABLE IF NOT EXISTS Human_res (
# work_id INT PRIMARY KEY,
# First_name varchar(45),
# Last_name varchar(45),
# email varchar(45),
# salary decimal
# )
# """

# cursor.execute(create_table_query)
try:
    # insert_que()  # - Calling the insert function
    select_que() # - Calling the select function
    # del_query() # - Calling the delete function
    update_que() # - Calling the update function
except TypeError:
    print("Invalid Data Inputted")



