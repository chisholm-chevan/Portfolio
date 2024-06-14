"""
Assignment Question 5: Student Database Management System Case Study
1. Lists:

Use a list to store the names of courses available in a school.
2. Tuples:

Create tuples to represent information about students (name, age, and courses enrolled).
3. Sets:

Use sets to store the unique courses that students are enrolled in.
4. Dictionaries:

Maintain a dictionary to store information about each student, where the student's name is the key.
5. Operations:

Implement operations to add a new student, display student information, and update courses enrolled.
The program should satisfy the following logic

The courses_available list stores the names of courses available in the school.
The students dictionary stores information about each student, with the student's name as the key and a tuple containing the name, age, and courses enrolled as the value.
Functions are used to display available courses, display student information, add a new student, and update courses enrolled for a student.
The program utilizes a loop to repeatedly present the user with a menu for different operations.

"""

# Use a list to store the names of courses available in a school.
sch_course = ["Law", "Computer Science", "Psychology", "Business Administration", "Mechanical Engineering", "Biology"]

# Create tuples to represent information about students (name, age, and courses enrolled).
dtb_students = (
    ('Tyrone Marshall', 23, sch_course[0], sch_course[5]), ('Jessica Pearson', 26, sch_course[1], sch_course[4]),
    ('Martin Dawson', 25, sch_course[2], sch_course[3]), ("John Black", 27, sch_course[3], sch_course[2]),
    ("Stacey Brown", 26, sch_course[4], sch_course[1]))

# Use sets to store the unique courses that students are enrolled in.
student1_courses = {sch_course[0], sch_course[5]}
student2_courses = {sch_course[1], sch_course[4]}
student3_courses = {sch_course[2], sch_course[3]}
student4_courses = {sch_course[3], sch_course[2]}
student5_courses = {sch_course[4], sch_course[1]}

# Maintain a dictionary to store information about each student, where the student's name is the key.
# the name, age, and courses enrolled as the value.
student_info = {"Tyrone Marshall": ("Tyrone Marshall", dtb_students[0][1], student1_courses),
                "Jessica Pearson": ("Jessica Pearson", dtb_students[1][1], student2_courses),
                "Martin Dawson": ("Martin Dawson", dtb_students[2][1], student3_courses),
                "John Black": ("John Black", dtb_students[3][1], student4_courses),
                "Stacey Brown": ("Stacey Brown", dtb_students[4][1], student5_courses)}


def display_student_records():
    if not dtb_students:
        print("No Student records found.")
    else:
        print("Student Records:")
        for index, record in enumerate(dtb_students, start=1):
            name, age, c1, c2 = record
            print(f"{index}. Name: {name}, Course 1: {c1}, Course2 : {c2}")


def printt():
    k = 1
    print("These are the available courses in the school:")
    for i in sch_course:
        print(str(k) + "-" + i)
        k = k + 1


while True:
    print("Welcome to our Student Database Management System")
    printt()
    print("Do you want to: \n1. Enter a new Student information\n2. Delete Student information\n3. View Current "
          "Students\n4. Exit the code")
    choice = int(input(": "))
    if choice == 1:
        new = 0
        print("How many new students do you want to add: ")
        m = int(input())
        while new < m:
            name = input("Please Enter your Full name: ")
            age = int(input("Please enter your Age: "))
            c1 = input("Please select your first course Subject: ")
            c2 = input("Please select your second course Subject: ")
            student_data = [name, age, c1, c2]
            y = list(dtb_students)
            y.append(student_data)
            print(y)
            print("Student Added Successfully")
            new += 1
            print("\n")
    elif choice == 2:
        print("Carefully type the name of student you would like to delete")
        y = list(dtb_students)
        print(y)
        del_stud = input()
        if del_stud == y[0][0]:
            del y[0]
            print("Record Successfully deleted")
            print(y)
            print("\n")
        elif del_stud == y[1][0]:
            del y[1]
            print("Record Successfully deleted")
            print(y)
            print("\n")
        elif del_stud == y[2][0]:
            del y[2]
            print("Record Successfully deleted")
            print(y)
            print("\n")
        elif del_stud == y[3][0]:
            del y[3]
            print("Record Successfully deleted")
            print(y)
            print("\n")
        elif del_stud == y[4][0]:
            del y[4]
            print("Record Successfully deleted")
            print(y)
            print("\n")
        else:
            raise Exception("Invalid Input")
    elif choice == 3:
        display_student_records()
        print("\n")
    elif choice == 4:
        print("You have exited the code")
        break

""" 
while True:
    sch_course = ["Law", "Computer Science", "Psychology", "Business Administration", "Mechanical Engineering", "Biology"]

    print("Welcome to your to do list application do you want to:\n1.Add items to your list\n2.Delete items for your list"
      "\n3.View current list")
    x = int(input(": "))
    if x == 1:
        print("What task would you like to add to your list?")
        y = input()
        listt.append(y)
        printt()
    elif x == 2:
        printt()
        print("What task would you like to remove from your list")
        p = int(input(": "))
        if p == 1:
            del listt[0]
            printt()
        elif p == 2:
            del listt[1]
            printt()
        elif p == 3:
            del listt[2]
            printt()
        elif p == 4:
            del listt[3]
            printt()
    elif x == 3:
        print("Here is your current To-Do list")
        printt()
"""

# CASE STUDY ON TUPLES-------------------------------------------------------------------------------------
# Python code to manage student records
"""
dtb_students = (('Tyrone', 16, 'Grade 10'), ('Jessica', 16, 'Grade 10'), ('Martin', 15, 'Grade 09'))

print("\tWelcome to The Student Database System")
print("1.Add New Student\n2.Delete a Student\n3.Search Student Information")
x = int(input(": "))
if x == 1:
    print("Please enter the name of the student")
    name = input()
    print("Please enter the age of the student")
    age = int(input())
    print("Please enter the Grade level of the student")
    grade = input()
    std1 = [name,age,grade]
    y = list(dtb_students)
    y.extend(std1)
    print(y)
elif x == 2:
    y = list(dtb_students)
    print("Please enter the name of the student you would like to delete")
    v = input()
    if v == y[0][0]:
        del y[0]
        print("1 Name deleted: New Student Database below:")
        print(y)
    elif v == y[1][0]:
        del y[1]
        print("1 Name deleted: New Student Database below:")
        print(y)
    elif v == y[2][0]:
        del y[2]
        print("1 Name deleted: New Student Database below:")
        print(y)
elif x == 3:
    print("Please enter the name of the student to see his information")
    u = input()
    if u == y[0][0]:
        print(f"The Student name is{y[0][0]}, here is their information: ")
        print(y[0])
    elif u == y[1][0]:
        print(f"The Student name is{y[1][0]}, here is their information: ")
        print(y[1])
    elif  u == y[2][0]:
        print(f"The Student name is{y[2][0]}, here is their information: ")
        print(y[2])
else:
    print("Invalid Name input")
"""
