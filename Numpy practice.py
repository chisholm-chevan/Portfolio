import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(a)

b = np.array(([1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]))
# print(b)

# Get Dimension
# print(a.ndim)
# print(b.ndim)

# Get Shape
# print(a.shape)
# print(b.shape)

# Get type
# print(a.dtype)
# print(b.dtype)

# Get Itemsize
# print(a.itemsize)
# print(b.itemsize)

# Accessing/Changing specific elements, rows, columns, etc
# Get a specific element
# print(b[1, 4])

# Get a specififc row
# print(b[0, :])  # prints the first row
# print(b[1, :])  # prints the second row

# startindex:endindex:stepsize
# print(b[0, 1:6:2])

b[1, 5] = 20
# print(b)

b[:, 2] = 5
# print(b)
# print("\n")

# Indexing 3D array (work outside in)
c = np.array([[[1, 2], [3, 4], [5, 6], [7, 8]]])
# print(c)
# print(c[0, 2, 0])

# Initializing Different Types of Arrays
# All 0s matrix
# i = np.zeros((2, 2, 2), float)
# print(i)

# All 1s matrix
# i = np.ones((2, 2, 2), float)
# print(i)

# Any other number
# i = np.full((2, 2), 99)
# print(i)

# Any other number (Full like)
# i = np.full_like(a, 4)
# cprint(i)

# Random decimal numbers
# i = np.random.rand(4, 2, 3)

# Random integer values
# i = np.random.randint(-4, 8, (3, 3))
# print(i)

# The identity Matrix
# i = np.identity(5)
# print(i)

# Repeat an Array
# arr = np.array([[1, 2, 3]])
# r1 = np.repeat(arr, 3, axis=0)
# print(r1)


# Sorting Arrays
# Sorting 1-Dimensional Arrays
array1 = np.array([1, 2, 3, 4, 5, 6, 7, -9, 21, -2, -1, 0])
array_sorted = np.sort(array1)
print(array_sorted)

# Sorting 2-Dimensional Arrays
array2 = np.array([[1, 2, 3], [4, 5, 6], [7, -9, 21], [-2, -1, 0]])
array_sorted2 = np.sort(array2)
print(array_sorted2)

# Sorting Boolean Arrays
array_bool = np.array([False, True, True, False, True, False, True])
array_sort_bool = np.sort(array_bool)
print(array_sort_bool)

# Sorting Array String
array_st = np.array(['A', 'B', 'C', 'H', 'Z', 'Y', 'M'])
array_sort_st = np.sort(array_st)
print(array_sort_st)

# Search sorted array
# This array function finds the location in which the value on the right which is '6' should be located
array3 = np.array([1, 3, 5, 7])
location = np.searchsorted(array3, 6)
print(location)

# Multiple values
location2 = np.searchsorted(array3, [2, 4, 6])
print(location2)

# Basic Computations in array
# Adding
w = np.arange(5)
aa = np.array([5, 6, 7, 8, 9])
print(w + aa)  # Produces [5 7 9 11 13]

# Subtracting
print(aa - w)  # Produces [5 5 5 5 5]

# Square
print(aa ** 2)  # Produces [25 36 49 64 81]

# Square root function
print(np.sqrt(aa))

# Multiply
print(aa * 3)

# Converting decimal to float
aaa = [1, 2, 3, 4]
print("Original array")
print(aaa)
xx = np.asfarray(aaa)
print("Array converted to a float type:")
print(xx)

r = np.ones((5, 5))
print(r)
r[1:-1, 1:-1] = 0
# Before the ',' we are assigning zeros to rows and after the ',' we are assigning zeros to columns
print(r)

# Comparing to arrays to see if a value is present in the other
array11 = np.array([0, 10, 20, 40, 60])
array12 = np.array([40, 60])

print("Array11:", array11)
print("Array12:", array12)
print("Compare each element of array1 and array2")
print(np.in1d(array11, array12))

# To get the unigue elements within an array - No Duplicates
array111 = np.array([10, 10, 20, 20, 30, 30])
print("Original array:")
print(array111)
print("Unique elements of the above array:")
print(np.unique(array111))