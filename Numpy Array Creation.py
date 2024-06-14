"""
1. NumPy Array Creation:

Use NumPy arrays to store exam scores for multiple students in different subjects.
2. NumPy Operations:

Calculate average scores for each student and each subject.Identify the highest and lowest scores in each subject.
3. Statistical Analysis:

Use NumPy functions for statistical analysis, such as calculating mean and standard deviation.

Considerations
The exam_scores NumPy array stores exam scores for multiple students in different subjects.
Functions are used to perform operations on the NumPy array, such as calculating average scores for each student and each subject, identifying the highest and lowest scores in each subject, and conducting statistical analysis.
NumPy functions like np.mean, np.max, np.min, and np.std are employed for array operations and statistical analysis.

"""

import numpy as np


# NumPy Array Creation
def create_exam_scores(num_students, num_subjects):
    # Create a NumPy array with random exam scores between 0 and 100
    exam_scores = np.random.randint(0, 101, size=(num_students, num_subjects))
    return exam_scores


# NumPy Operations
def calculate_average_scores(exam_scores):
    # Calculate average scores for each student (row-wise)
    student_avg_scores = np.mean(exam_scores, axis=1)

    # Calculate average scores for each subject (column-wise)
    subject_avg_scores = np.mean(exam_scores, axis=0)

    return student_avg_scores, subject_avg_scores

def identify_highest_and_lowest_scores(exam_scores):
    # Identify the highest scores in each subject
    highest_scores = np.max(exam_scores, axis=0)

    # Identify the lowest scores in each subject
    lowest_scores = np.min(exam_scores, axis=0)

    return highest_scores, lowest_scores

# Statistical Analysis
def statistical_analysis(exam_scores):
    # Calculate the mean and standard deviation of all scores
    overall_mean = np.mean(exam_scores)
    overall_std = np.std(exam_scores)

    return overall_mean, overall_std

# Example usage
num_students = 5
num_subjects = 3

# Create exam scores for students in different subjects
exam_scores = create_exam_scores(num_students, num_subjects)

# Display the exam scores
print("Exam Scores:")
print(exam_scores)

# Calculate average scores for each student and each subject
student_avg_scores, subject_avg_scores = calculate_average_scores(exam_scores)
print("\nAverage Scores (per student):", student_avg_scores)
print("Average Scores (per subject):", subject_avg_scores)

# Identify the highest and lowest scores in each subject
highest_scores, lowest_scores = identify_highest_and_lowest_scores(exam_scores)
print("\nHighest Scores (per subject):", highest_scores)
print("Lowest Scores (per subject):", lowest_scores)

# Statistical Analysis
overall_mean, overall_std = statistical_analysis(exam_scores)
print("\nOverall Mean:", overall_mean)
print("Overall Standard Deviation:", overall_std)


"""
# Five students with 3 subjects
from numpy import *
import numpy as np

print("What is your name")
name = input()
mark1 = int(input("Enter your first exam score"))
mark2 = int(input("Enter your first exam score"))
mark3 = int(input("Enter your first exam score"))
exam_score = np.zeros((mark3, mark2, mark1))
print(exam_score)
"""