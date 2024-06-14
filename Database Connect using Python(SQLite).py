"""
Assignment Question 2: Database Connectivity using Python (SQLite)
Task 1: Database Setup
Create an SQLite database file named "company.db" with a table named "employees." The "employees" table should have the following columns: id (integer, primary key), name (text), position (text), and salary (real).
Task 2: Data Insertion
Write a Python script to insert at least five records into the "employees" table. The data should include names, positions, and salaries. Use parameterized queries to avoid SQL injection.
Task 3: Data Retrieval and Analysis
a) Implement a function to retrieve and display all employees and their details from the "employees" table.
b) Implement a function to calculate and display the average salary of all employees.
Task 4: Update Operation
Write a function to update the position of an employee based on their ID. Prompt the user to input the employee ID and the new position.
Task 5: Exception Handling
Include appropriate exception handling in your script. Handle cases such as database connection errors, query execution errors, and user input validation errors.
Submission Guidelines:
Submit a well-organized Python script with clear comments explaining the purpose of each section.
Include SQL statements used for creating the database and table in a separate SQL file (e.g., "create_tables.sql").
Provide a README file with instructions on how to run your script and any additional notes about your implementation.
"""
# Task 1: Database Setup
import mysql.connector  # - Importing the SQL library to create a connection with MSQL database
from mysql.connector import errorcode
database = "company"
try:
    mydb = mysql.connector.connect(host='local', user='root', password='Generalboy$1', database="company")
    cursor = mydb.cursor()  # - A cursor allows us to interact with the database through queries. Acts like a mouse/keyboard

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Access denied: Check your username and password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist.")
    else:
        print(f"MySQL Error: {err}")

def create_dtb():  # A function to create Databases
    cursor.execute("CREATE DATABASE company ".format(database))  # Creating the database file from the python end.
    cursor.execute("USE company".format(database))
    # This function Switches to the newly created database that is being created from the SQL side. (Within the mydb
    # connection in line 24 - the "database" module is being replaced with the variable "database" above in Line 22
    # It is then added afterward to the mydb connection in Line 24 to perform query functions.



def create_tb():  # A function to create tables
    create_table_query = """ CREATE TABLE IF NOT EXISTS employees(
                    ID_num INT PRIMARY KEY,
                    NAME varchar(45),
                    position_ varchar(45),
                    salary real
                    ); """
    cursor.execute(create_table_query)  # Creating the Table within the database


# Task 2: Data Insertion
def insert_que():
    global id_num, name, position, salary, insert_data_query, user_data
    print("How many Employees would you like to enter into the Company's database")
    num = int(input(": "))
    k = 0
    while k < num:
        id_num = int(input("Please enter your ID number - This is a 3 digit number - Starting with 1: "))
        name = input("Please enter your Full Name: ")
        position = input("Please enter the position you currently hold: ")
        salary = float(input("Please enter your salary amount for the current year: "))
        k += 1
        print("-----------------------------------------------------------------------------")
        insert_data_query = """ INSERT INTO employees (ID_num, NAME, position_, salary) values (%s, %s, %s, %s)"""
        # user_data = [(id_num, name, position, salary)]
        cursor.execute(insert_data_query, (id_num, name, position, salary))
        mydb.commit()  # - This allows us to confirm the changes made via the queries on the database side of connection
        print("Data Inserted Successfully")


# Task 3: Data Retrieval and Analysis
def select_que():  # A function to retrieve and display all employees and their details from the employees table
    cursor.execute("SELECT * FROM EMPLOYEES")
    results = cursor.fetchall()
    for row in results:
        print(row)


def delete_que():  # A function to delete a row or rows employees and their details from the employees table
    print("Please enter the ID number of the first employee you want to delete")
    y = int(input())
    print("Please enter the ID number of the second employee you want to delete")
    x = int(input())
    delete_data_query = " DELETE FROM employees WHERE ID_num = %s and %s"
    cursor.execute(delete_data_query, (y, x))
    mydb.commit()
    print("Data Deleted Successfully")


def calc():  # A function to calculate the total average salaries for  all employees.
    cursor.execute(" SELECT avg(salary) as TOTAL_AVG_SALARY FROM EMPLOYEES")
    results = cursor.fetchall()
    for row in results:
        print("The Total Average Salary for each employee is:", row)


# Task 4: Update Operation
def update_que():  # A function to update any given row within the "employees" table.
    same_id = int(input("Please enter your Identification number: "))
    new_pos = input("Please enter the new position you have for 2023: ")
    update_data_query = "UPDATE employees SET position_ = %s WHERE ID_num = %s"
    cursor.execute(update_data_query, (new_pos, same_id))
    mydb.commit()
    print("Data Updated Successfully")

# ---------------------------------------------MAIN PROGRAM----------------------------------------------------
# insert_que()
# delete_que()
# select_que()
# calc()
# update_que()
