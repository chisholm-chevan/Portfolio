import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)
print(np.shape(arr))
print(np.ndim(arr))
print(arr[1, 1, 1])

arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
new_arr1 = arr1.reshape(2, 2, -1)
print(new_arr1)

# Boolean Masking and Indexing
array1 = np.array([1, 2, 4, 9, 11, 16, 18, 22, 26, 31, 33, 47, 51, 52])
# create a boolean mask using combined logical operators
boolean_mask = (array1 < 10) | (array1 > 40)
# apply the boolean mask to the array
result = array1[boolean_mask]
print(result)
# Output: [ 1 2 4 9 47 51 52]
arr2 = np.array([1, 2, 4, 5, 6, 7])
boolean_mask = arr2 % 2 == 0
result = arr2[boolean_mask]
print(result)

arr2 = np.array([1, 2, 4, 5, 6, 7])
arr2_copy = arr2.copy()
boolean_mask = arr2 % 2 == 0
arr2_copy[boolean_mask] = 0
print(arr2_copy)
print("-------------------------------------------------------------------------")
# Fancy Indexing
x = np.array([1, 67, 38, 46, 55, 63, 97, 82, 91, 104])
y = [0, 3, 4, 7]
print(x[y])

# Another way to fancy index
array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# select a single element
simple_indexing = array1[3]
print("Simple Indexing:", simple_indexing)  # 4
# select multiple elements
fancy_indexing = array1[[1, 2, 5, 7]]
print("Fancy Indexing:", fancy_indexing)  # [2 3 6 8]

# Assign new values using fancy indexing
array1 = np.array([3, 2, 6, 1, 8, 5, 7, 4])
# create a list of indices to assign new values
indices = [1, 3, 6]
# create a new array of values to assign
new_values = [10, 20, 30]
# use fancy indexing to assign new values to specific elements
array1[indices] = new_values
print(array1)
# Output: [ 3 10 6 20 8 5 30 4]

# Fancy Indexing with Ndarrays
# create a 2D array
array1 = np.array([[1, 3, 5],
                   [11, 7, 9],
                   [13, 18, 29]])
# create an array of row indices
row_indices = np.array([0, 2])
# use fancy indexing to select specific rows
selected_rows = array1[row_indices, :]
print(selected_rows)

# Combined Indexing
u = np.arange(12).reshape(3, 4)  # creating arrays using arange and reshape
print(u)
print(u[2, [2, 0, 1]])

# Modifying values using Fancy indexing
x = np.arange(10)
i = np.array([2, 1, 8, 4])
x[i] = 99
print(x)  # result - [ 0 99 99  3 99  5  6  7 99  9]

# Sorting in Numpy--------
a = np.array([9, 3, 1, 7, 4, 3, 6])
# unsorted array print
print("Original array:\n", a)
# Sort array indices
b = np.argsort(a)
print("Sorted indices of original array->", b)

# To get sorted array using sorted indices
# c is temp array created of same len as of b
c = np.zeros(len(b), dtype=int)
for i in range(0, len(b)):
    c[i] = a[b[i]]
print("Sorted array->:", c)

ap = np.arange(6).reshape(2, 3)
print(ap)
print("------")
# print(np.sort(ap, axis=0, kind="quicksort", order=None))  # This would be the long way how to sort an array
# print(np.sort(ap, axis=0, kind="mergesort", order=None)) If you need a stable sort use this
# print(np.sort(ap, axis=0, kind="heapsort", order=None)) If Memory is a concern use this

print(np.sort(ap, axis=-1))  # This is the default way that the computer sorts
print(np.sort(ap, axis=1))  # This isn't the default way but it sorts in ascending order
print(np.sort(ap, axis=None))  # This sorting method flattens the array

# Structured Array
data_type = [("name", 'U15'), ("class", int), ("height", float)]
student_details = [("Mike", 1, 188.8), ("James", 2, 108.8), ("Stanley", 3, 198.8), ("Luke", 4, 128.8)]
student = np.array(student_details, dtype=data_type)
print(student)
print(np.sort(student, order="height"))

# Write a NumPy program to create a structured array from given student
# name, height, class and their data types. Now sort by class, then height if
# class are equal.

data_type = [("name", "U15"), ("height", float), ("class", int)]
# When assigning string datatype use 'U' instead of 'S' e.g 'U15' this won't print 'b' beside the strings
student_details = [("Dave", 158.0, 5), ("David", 168.9, 4), ("Chris", 177.9, 3), ("Brown", 174.9, 2)]
student = np.array(student_details, dtype=data_type)
print(np.sort(student, order=("class", "height")))

# Write a NumPy program to sort the student id with increasing height of the
# students from given students id and height. Print the integer indices that
# describes the sort order by multiple columns and the sorted data.

student_id = np.array([1923, 2345, 5653, 8466, 4635, 8907, 2463])
student_height = np.array([188.0, 172.0, 199.0, 145.0, 177.0, 192.0, 190.0])
indices = np.lexsort((student_id, student_height))
print("Sorted Data:")
for n in indices:
    print(student_id[n], student_height[n])

# Write a NumPy program to get the indices of the sorted elements of a
# given array.

student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])

# Displaying the original array
print("Original array:")
print(student_id)

# Sorting the indices of the array&#39;s elements in ascending order
a = np.sort(student_id)
i = np.argsort(student_id)

# Displaying the indices of the sorted elements
print("Indices of the sorted elements of a given array:")
print(i)
print(a)

# Aggregations in structured array
a = np.dtype([('Name', 'U20'), ('Age', np.int32), ('grade', np.float16)])
data = np.array([("Alice", 25, 4.8), ("Bob", 23, 3.9), ("Charlie", 27, 4.5)], dtype=a)
sorted_data = np.sort(data, order='Age')[::-1]
print(sorted_data)

# Aggregations
average_age = np.mean(data['Age'])
maximum_grade = np.max(data['grade'])
print(average_age)
print(maximum_grade)

"""
# Filtering
filtered_data = data[data.Age < 26]
print(filtered_data)
"""

# Define the custom data type with a nested list data type
employee_dtype = [('name', 'U20'), ('age', np.int16), ('projects', 'O')]  # Use 'O' for object arrays

# Create sample data
employee_data = [
    ('Alice', 30, ['Project A', 'Project B']),
    ('Bob', 25, ['Project C']),
    ('Charlie', 40, ['Project D', 'Project E', 'Project F'])
]
# Create the structured array
employee_array = np.array(employee_data, dtype=employee_dtype)
# Access and manipulate data

print("Employee names:", employee_array['name'])
print("Projects for Bob:", employee_array[1]['projects'])
# Find employees working on Project A
project_a_employees = employee_array[employee_array['projects'] == 'Project A']
print("Employees working on Project A:", project_a_employees['name'])
