import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='Generalboy$1', database='banking_system')

cursor = mydb.cursor()

"""
create_table_query = """
# CREATE TABLE IF NOT EXISTS grading (
# id INT PRIMARY KEY,
# First_name varchar(45),
# Last_name varchar(45),
# Math INT,
# Biology INT,
# Chemistry INT
# )
"""
"""

# cursor.execute(create_table_query)

"""
insert_data_query = """
# INSERT INTO grading (id, First_name, Last_name, Math, Biology, Chemistry) VALUES (%s, %s, %s, %s, %s, %s)
"""
user_data = [(100, "Michael", "Thomas", 93, 78, 89),
             (101, "Larry", "O'Brien", 85, 65, 96),
             (102, "David", "Thomas", 77, 78, 81),
             (103, "Lucy", "Duck", 45, 56, 81),
             (104, "Mark", "Twain", 99, 98, 97),
             (105, "Matthew", "Barker", 96, 95, 94),
             (106, "Luke", "Modric", 93, 92, 91),
             (107, "John", "Brown", 90, 89, 88),
             (108, "Peter", "Franklin", 87, 86, 85),
             (109, "Marcus", "Rashford", 84, 83, 82),
             (110, "Alejandro", "Garnacho", 81, 80, 79),
             (111, "Kevin", "Debruyne", 78, 77, 76),
             (112, "Phil", "Foden", 75, 74, 73),
             (113, "Jimmy", "Boy", 72, 71, 70),
             (114, "James", "Brown", 69, 68, 67),
             (115, "Alejandro", "Garnacho", 65, 64, 63),
             (116, "Sasha", "Brown",62, 61, 60),
             (117, "Maliqua", "Black", 59, 58, 57),
             (118, "Trishauna", "Robinson", 56, 55, 54),
             (119, "Aliah", "Brown", 53, 52, 51),
             (120, "Luciel", "Williams", 50, 49, 48),
             (121, "That", "Girl", 47, 46, 45),
             (122, "Pretty", "Boy", 44, 43, 42),
             (123, "Optimus", "Prime", 41, 40, 39),
             (124, "Bumble", "Bee", 38, 37, 36),
             (125, "Bruno", "Fernandes", 35, 80, 34),
             (126, "Harry", "Maguire", 78, 33, 76),
             (127, "Johnny", "Evans", 31, 74, 32),
             (128, "Varnae", "Raphael", 30, 71, 29),
             (129, "Luke", "Shaw", 69, 27, 28),
             (130, "Aaron", "WanBissaka", 26, 80, 25),
             ]
"""

# cursor.executemany(insert_data_query, user_data)
# mydb.commit()

"""
cursor.execute("SELECT * FROM grading")
results = cursor.fetchall()
for row in results:
    print(row)
"""

cursor.execute("SELECT MIN(Math), MIN(Biology), MIN(Chemistry) from grading ")
results = cursor.fetchall()
for row in results:
    print("Minimum Marks for Math, Biology and  Chemistry")
    print(row)

cursor.execute("SELECT MAX(Math), MAX(Biology), MAX(Chemistry) from grading")
results = cursor.fetchall()
for row in results:
    print("Maximum Marks for Math, Biology and  Chemistry")
    print(row)
    print("\n")

cursor.execute("SELECT sum(Math), sum(Biology), sum(Chemistry) from grading ")
results = cursor.fetchall()
for row in results:
    print("The Total Accumulated  Marks for Math, Biology and  Chemistry")
    print(row)
    print("\n")

cursor.execute("SELECT AVG(Math), AVG(Biology), AVG(Chemistry) from grading ")
results = cursor.fetchall()
for row in results:
    print("The Average for Math, Biology and  Chemistry")
    print(row)
    print("\n")

cursor.execute("""SELECT id, First_name, Last_name, avg(Math), avg(Biology), avg(Chemistry), 
    CASE 
        WHEN (avg(Math) + avg(Biology) + avg(Chemistry))/3 >= 90 THEN 'A+'
        WHEN (avg(Math) + avg(Biology) + avg(Chemistry))/3 < 90 >= 80 THEN 'A'
        WHEN (avg(Math) + avg(Biology) + avg(Chemistry))/3 < 80 >= 70  THEN 'B'
        WHEN (avg(Math) + avg(Biology) + avg(Chemistry))/3 < 70 >= 60 THEN 'C'
        WHEN (avg(Math) + avg(Biology) + avg(Chemistry))/3 < 60 THEN 'D'
        ELSE 'F' END AS MARKING_SYSTEM FROM grading GROUP BY ID ORDER BY MARKING_SYSTEM
               """)
results = cursor.fetchall()
print("Query showing the Final Grade for all 3 Subjects for each student")
for row in results:
    print(row)

cursor.close()
mydb.close()
