class DataAnalytic:
    attr1 = "Student"
    attr2 = "SQL"

    # A sample method
    def func(self):
        print("I'm a", self.attr1)
        print("I learn about", self.attr2)


# Object instantiation
Obj = DataAnalytic()

# Accessing class attributes
# and method through objects
print(Obj.attr1)
print(Obj.attr2)
Obj.func()
# -------------------------------------------------------------------------------------------------------
print("------------Program 2 ----------------------------")


class DataAnalytic:

    def __init__(self, course, tech):  # Constructor
        self.course = course
        self.tech = tech
        print("Variables are " + self.course + " and " + self.tech)

    def show(self):
        print("Hello, I m doing " + self.course + " and I" +
              " Learn " + self.tech + ".")


print("-------Program2------------")
obj1 = DataAnalytic("DataAnalytic", "SQL")
obj2 = DataAnalytic("Mobile Application", "Android")
obj1.show()
obj2.show()
# -------------------------------------------------------------------
print("---------------------Program 3----------------------")


class DataAnalytic:

    def __init__(abc, course, tech):  # Constructor
        abc.course = course
        abc.tech = tech

    def show(abc):
        print("Hello, I m doing " + abc.course + " and I" +
              " Learn " + abc.tech + ".")


print('-----------Program3------------')
obj = DataAnalytic("DataAnalytic", "SQL")
obj.show()
# -------------------------------------------------------------------
print("------------------------Program 4 ----------------------")


class Training:
    # Class Variable
    trainee = 'Trainee'

    # The init method or constructor
    def __init__(self, course, subject):
        # Instance Variable
        self.course = course
        self.subject = subject


# Objects of Dog class
Stud1 = Training("Data Analytics", "SQL")
Stud2 = Training("Mobile Application", "Android")

print('Student 1 details:')
print('Student 1 is a', Stud1.trainee)
print('course: ', Stud1.course)
print('subject: ', Stud1.subject)

print('\nStudent 2 details:')
print('Student 2 is a', Stud2.trainee)
print('course: ', Stud2.course)
print('subject: ', Stud2.subject)

# Class variables can be accessed using class
# name also
print("\nAccessing class variable using class name")
print(Training.trainee)


# ---------------------------
class Comp:
    a: int
    b: int

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self, a, b):
        return self.a + self.b

    def sub(self, a, b):
        return self.a - self.b

    def div(self, a, b):
        return self.a / self.b

    def mul(self, a, b):
        return self.a * self.b


print("Enter a number")
x = int(input())
print("Enter a second number")
y = int(input())

efg = Comp(x, y)
print(efg.add(x, y))
print(efg.mul(x, y))
print(efg.div(x, y))
print(efg.sub(x, y))
