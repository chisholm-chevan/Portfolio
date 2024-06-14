import mysql.connector
import sqlite3
database = "new_database"

mydb = mysql.connector.connect(host="localhost", user="root",
                               password="Generalboy$1",
                               database="new_database")
cursor = mydb.cursor()


def create_datab():
    cursor.execute("CREATE DATABASE new_database".format(database))
    cursor.execute("USE new_database".format(database))


def create_tb():
    create_table_query = """CREATE TABLE EMPLOYEE_Table(
    emp_id INT PRIMARY KEY,
    First_Name VARCHAR(45),
    Last_Name VARCHAR(45),
    position_ VARCHAR(45)
    );
    """
    cursor.execute(create_table_query)


def insert_val():
    global lname, fname, emp_id, insert_data, position
    print("How many new employees would you like to enter into the new database: ")
    x = int(input())
    q = 0
    while q < x:
        fname = input("Please enter your First name: ")
        lname = input("Please enter you Last name: ")
        while True:
            try:
                emp_id = int(input("Enter a your Employee ID (3 digits starting with 1): "))

                # Check if the number has exactly 3 digits and starts with 1
                if 100 <= emp_id <= 199:
                    print(f"You entered a valid Employee ID: {emp_id}")
                    break
                else:
                    print("Invalid input. Please enter a 3-digit number starting with 1.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        position = input("Please enter your new position at work: ")
        q += 1
        insert_data = """ Insert INTO EMPLOYEE_Table VALUES (%s, %s, %s, %s)"""
        cursor.execute(insert_data, (emp_id, fname, lname, position))
        mydb.commit()
        print("Data Inserted Successfully")


def select_data():
    cursor.execute(" SELECT * FROM EMPLOYEE_Table")
    results = cursor.fetchall()
    for row in results:
        print(row)


select_data()
mydb.close()
