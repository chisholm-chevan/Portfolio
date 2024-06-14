import numpy as np


# Create NumPy arrays for student information
students = np.array(['John', 'Jane', 'Bob', 'Alice'])
subjects = np.array(['Math', 'English', 'Science'])
grades = np.array([
    [75, 80, 90],
    [85, 88, 92],
    [60, 70, 75],
    [92, 95, 89]
])

# Create a dictionary using student names as keys
student_dict = {name: grades[i] for i, name in enumerate(students)}
print(student_dict)

# Find the average per student and per subject
average_per_student = np.mean(grades, axis=1)
average_per_subject = np.mean(grades, axis=0)

# Find students with averages over 80 and under 50
students_over_80 = students[average_per_student > 80]
students_under_50 = students[average_per_student < 50]

# Find the total average for the school
total_school_average = np.mean(grades)

# Print the results
print("Average per student:")
for name, avg in zip(students, average_per_student):
    print(f"{name}: {avg:.2f}")

print("\nAverage per subject:")
for subject, avg in zip(subjects, average_per_subject):
    print(f"{subject}: {avg:.2f}")

print("\nStudents with averages over 80:", students_over_80)
print("Students with averages under 50:", students_under_50)

print("\nTotal average for the school:", total_school_average)