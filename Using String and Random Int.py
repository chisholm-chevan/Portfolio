import random as ran
import string

def text(length):
    # Print the string in Uppercase
    wrd1 = ''.join((ran.choice(string.ascii_uppercase) for x in range(length)))  # run the loop until the define length
    print("Before you proceed type TEXT on screen: ", wrd1)
    wrd2 = input(":  ")
    if wrd2 == wrd1:
        print("Captcha is correct")
        print("\n")
    else:
        print("Captcha is, Wrong: You are a Robot, Try Again")
        print("\n")
        text(length)
        print("\n")

def alphnum():
    S = 10  # number of characters in the string.
    # call random.choices() string module to find the string in Uppercase + numeric data.
    rann = ''.join(ran.choices(string.ascii_uppercase + string.digits, k=S))
    print("Before you proceed type the Alphanumerics on screen : " + str(rann))  # print the random data
    numtxt = input(": ")
    if rann == numtxt:
        print("Captcha is correct, Proceed")
        print("\n")
    else:
        print("Captcha is, Wrong: You are a robot, Try Again")
        print("\n")
        alphnum()
        print("\n")
def express():
    n = ran.randint(0, 1000)
    m = ran.randint(0, 1000)
    c = n + m
    print("Before you proceed please solve this equation")
    print(f"{n} + {m} ")
    o = int(input(": "))
    if o == c:
        print("Calculation is correct, please proceed")
    else:
        print("Captcha is, Wrong: You are a robot, Try Again")
        express()

while True:
    print("Captcha Testing: Please select any of the 4 options:\n1. Text\n2. Alphanumeric\n3. Expression\n4. Exit")
    p = int(input("Enter: "))
    e = 0

    if p > 4:
        raise Exception("Invalid Input Entered")
    elif p == 1:
        text(10)
    elif p == 2:
        alphnum()
    elif p == 3:
        express()
    elif p == 4:
        print("You have exited the code.")
        break
