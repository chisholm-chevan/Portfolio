import sqlite3

database = "brand_new"
mylite3 = sqlite3.connect(database)
cursor = mylite3.cursor()
print("Database created successfully")


def create_tb_store_supplier():
    try:
        create_table_query = """ CREATE TABLE store_supply(
            supplier_ID INTEGER PRIMARY KEY,
            supplier_name Text,
            supplier_address Text,
            products_ Text,
            cost_per_unit Real,
            quantity_ Real);"""
        cursor.execute(create_table_query)
        print("Table Created Successfully")
    except:
        mylite3.rollback()
        print("Error creating table")


def create_customer_table():
    try:
        create_table_query = """ CREATE TABLE customer
        (
            customer_ID INTEGER PRIMARY KEY,
            customer_name Text,
            customer_address Text
        )
            """
        cursor.execute(create_table_query)
        print("Table Created Successfully")
    except:
        mylite3.rollback()
        print("Error creating table")


def create_purchases_table():
    try:
        create_table_query = """ CREATE TABLE purchases
        (
            purchase_ID INTEGER PRIMARY KEY,
            items_purchased Text,
            amount_ordered Real,
            cost_accumulated Real,
            customer_ID INTEGER,
            FOREIGN KEY(customer_ID) REFERENCES customer(customer_ID) ON DELETE CASCADE
        )
            """
        cursor.execute(create_table_query)
        print("Purchases table Created Successfully")
    except:
        mylite3.rollback()
        print("Error creating table")


def insert_data_into_store_supply():
    try:
        records = [(100, "Sunshine Factory", "34 Gordon Street", "Snacks and Treats", 100, 200),
                   (101, "Grace Kennedy", "34 Gordon Street", "Tin Food Items", 150, 200),
                   (102, "Lasco Foods", "34 Gordon Street", "Food Drinks", 200, 200),
                   (103, "Ensure", "34 Gordon Street", "Food Drink and Supplements", 250, 200),
                   (104, "National Bakery", "34 Gordon Street", "Baked Goods", 700, 200)]
        cursor.executemany("Insert into store_supply VALUES (?,?,?,?,?,?)", records)
        mylite3.commit()
        print("Data Inserted Successfully")
    except:
        ValueError("Print incorrect data submitted")


def insert_data_into_customer():
    try:
        records = [(200, "John Brown", "56 Lime Street"),
                   (201, "Stacey Gray", "34 Down Street"),
                   (202, "Tammy Black ", "23 White Street")]
        cursor.executemany("Insert into customer VALUES (?,?,?)", records)
        mylite3.commit()
        print("Data Inserted into Customer Table Successfully")
    except:
        ValueError("Print incorrect data submitted")


def insert_data_into_purchases():
    try:
        records = [(300, "Brown Bread", 1, 700, 200),
                   (301, "Brown Bread", 1, 700, 200),
                   (302, "Brown Bread", 1, 700, 201),
                   (303, "Brown Bread", 1, 700, 202)]
        cursor.executemany("Insert into purchases VALUES (?,?,?,?,?)", records)
        mylite3.commit()
        print("Data Inserted into Purchases Table Successfully")
    except:
        ValueError("Print incorrect data submitted")


def select_data():
    cursor.execute("SELECT * FROM customer")
    results = cursor.fetchall()
    for row in results:
        print(row)


def count_query():
    cursor.execute("select count(supplier_name) from store_supply")
    results = cursor.fetchall()
    for row in results:
        print(row)


def drop_table():
    cursor.execute("DROP TABLE purchases")
    mylite3.commit()
    print("Table Dropped Successfully")

def select_limit_query():
    cursor.execute("select * from purchases ORDER BY purchase_id ASC LIMIT 1")
    first_row = cursor.fetchone()
    cursor.execute("select * from purchases ORDER BY purchase_id DESC LIMIT 1")
    last_row = cursor.fetchone()
    print("First Row:", first_row)
    print("Last Row:", last_row)


select_limit_query()
