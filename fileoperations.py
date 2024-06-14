# File Handling - 'r': Read a file, 'w': Write in/to a file, 'a': append to the bottom of the file
# f = open('Mydata.txt', 'r')

# Copying data from one file to another
"""
h = open('newfile', 'w')
for data in f:
    h.write(data)
"""

# 3.Program to write a message to a file
"""
h = open('newfile', 'w')
h.write("Hello World") 
h.write("How are you")
"""

"""
def file_read():
    txt = open('text.txt', 'r')
    print(txt.read())


file_read()
"""
"""
#Write a Python program to read first n lines of a file.
def file_read_from_head(fname, nlines):
    from itertools import islice
    with open(fname) as f:
        for line in islice(f, nlines):
            print(line)


file_read_from_head('text.txt', 2)
"""

"""
# Write a Python program to append text to a file and display the text.
def file_read():
    from itertools import islice
    txt = open('text.txt', 'a')
    txt.write('Python Exercises')
    txt.write('Java Exercises')

file_read()
"""
"""

# Write a Python program to read last n lines of a file.
import sys
import os


def file_read_from_tail(fname, lines):
    bufsize = 8192
    fsize = os.stat(fname).st_size
    iteri = 0
    with open(fname) as f:
        if bufsize > fsize:
            bufsize = fsize - 1
            data = []
            while True:
                iteri += 1
                f.seek(fsize - bufsize * iteri)
                data.extend(f.readlines())
                if len(data) >= lines or f.tell() == 0:
                    print(''.join(data[-lines:]))
                    break


file_read_from_tail('text.txt', 2)
"""

"""
# Write a python program to find the longest words.
def longest_word(filename):
    with open(filename, 'r') as infile:
        words = infile.read().split()
        max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]


print(longest_word('text.txt'))
"""

"""
# Write a python program to count the uppercase and lowercase characters
def count_up_low(file_name):
    try:
        with open(file_name, 'r') as file:
            uppercase_count = 0
            lowercase_count = 0
            for line in file:
                for char in line:
                    if char.isupper():
                        uppercase_count += 1
                    elif char.islower():
                        lowercase_count += 1
            print("The total number of Upper Case Letters: {}".format(uppercase_count))
            print("The total number of Lower Case Letters:".format(lowercase_count))
            
    except FileNotFoundError:
        print("Print File not found. Please provide a valid Path")
    except Exception as e:
        print("An error occurred", e)
        

file_name = "Mydata.txt"
count_up_low(file_name)
"""

"""
# Write a python code to copy the odd lines from one file to another
def copy_odd_files(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r') as input_file:
            with open(output_file_path, 'w') as output_file:
                lines = input_file.readlines()
                output_file.writelines(lines[::2])
        print(f"Odd lines copied from '{input_file_path}' to '{output_file_path}' successfully.")
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except Exception as e:
        print("An error occurred: ", e)


input_file_path = "newfile"
output_file_path = "Mydata.txt"
copy_odd_files(input_file_path, output_file_path)
"""

"""
def read_file_line_by_line(file_path):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read each line from the file using readline()
            line_number = 1
            while True:
                line = file.readline()
                # Break the loop if there are no more lines to read
                if not line:
                    break
                print(f"Line {line_number}: {line.strip()}")
                line_number += 1

    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except Exception as e:
        print("An error occurred:", e)


# Replace 'your_file.txt' with the actual path to your text file
file_path = 'your_file.txt'
read_file_line_by_line(file_path)
"""

"""
def count_lines(file_path):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Use a generator expression to count lines efficiently
            line_count = sum(1 for line in file)

        return line_count

    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except Exception as e:
        print("An error occurred:", e)


# Replace 'your_file.txt' with the actual path to your text file
file_path = 'Mydata.txt'
lines_count = count_lines(file_path)

if lines_count is not None:
    print(f"Number of lines in '{file_path}': {lines_count}")

my_list = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11]
print(my_list[-7:])
"""

f = None

for i in range(5):

    with open("data.txt", "w") as f:

        if i > 2:
            break

print(f.closed)
