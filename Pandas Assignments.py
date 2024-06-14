import pandas as pd
import numpy as np

"""
data = [1, 2, 3, 4, 5]
my_series = pd.Series(data)
print("One-dimensional array-like object (Series):")
print(my_series)
"""
"""
data = [1, 2, 3, 4, 5]
my_series = pd.Series(data)
my_list = my_series.tolist()
print("Python List:", my_list)
print("Type of the Python List:", type(my_list))
"""
"""
series1 = pd.Series([22, 44, 66, 88, 100])
series2 = pd.Series([11, 33, 55, 77, 99])

# Addition
add_result = series1 + series2

# Subtraction
sub_result = series1 - series2

# Multiplication
mul_result = series1 * series2

# Division
div_result = series1 / series2

# Displaying the results
print("Original Series 1:")
print(series1)

print("\nOriginal Series 2:")
print(series2)

print("\nAddition Result:")
print(add_result)

print("\nSubtraction Result:")
print(sub_result)

print("\nMultiplication Result:")
print(mul_result)

print("\nDivision Result:")
print(div_result)
"""

"""
series1 = pd.Series([2, 4, 6, 8, 10])
series2 = pd.Series([1, 3, 5, 7, 10])

# Comparing elements
equal_elements = series1 == series2
greater_elements = series1 > series2
less_elements = series1 < series2

# Displaying the comparison results
print("Original Series 1:")
print(series1)

print("\nOriginal Series 2:")
print(series2)

print("\nComparison - Equal Elements:")
print(equal_elements)

print("\nComparison - Greater Elements:")
print(greater_elements)

print("\nComparison - Less Elements:")
print(less_elements)
"""

"""
data = {'Name': ['John', 'Jane', 'Bob', 'Alice'],
        'Age': [25, 30, 22, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)
print(df)
"""

"""
data = {'Name': ['John', 'Jane', 'Bob', 'Alice'],
        'Age': [25, 30, 22, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

# Display the entire DataFrame
print("Original DataFrame:")
print(df)
print("\n")

# Using loc to select specific rows and columns
selected_data = df.loc[[1, 3], ['Name', 'City']]

# Display the selected data
print("Selected Data using loc:")
print(selected_data)
"""
"""
# Creating a DataFrame with custom index names
data = {'Name': ['John', 'Jane', 'Bob', 'Alice'],
        'Age': [25, 30, 22, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}

index_names = ['Person1', 'Person2', 'Person3', 'Person4']

df = pd.DataFrame(data, index=index_names)

# Display the DataFrame with index names
print("DataFrame with Index Names:")
print(df)
"""

"""
data = {'John': 25, 'Jane': 30, 'Bob': 22, 'Alice': 28}
ages_series = pd.Series(data, name='Age')

print("Original Series:")
print(ages_series)
print("\n")

print("Accessing elements by index:")
print("John's age:", ages_series['John'])
print("Alice's age:", ages_series['Alice'])
print("\n")

# Slicing the Series by index
print("Slicing the Series by index:")
print(ages_series[['John', 'Bob', 'Alice']])
print("\n")

# Filtering the Series based on conditions
print("Filtering the Series based on conditions:")
print(ages_series[ages_series > 25])
"""

# Create a python code with pandas that includes all off the following:
# 1) Creating a Data frame and selecting columns, 2) Selecting Rows Based on Condition,
# 3) Handling Missing Data, 4) Grouping and Aggregate data, 5) Merging Data frames,
# 6) Pivot Table, 7) Time Series
"""
# 1) Creating a Data frame and selecting columns
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
        'Age': [25, 30, 22, 35, 28],
        'Salary': [50000, 60000, 45000, 70000, 55000],
        'Department': ['HR', 'IT', 'Finance', 'IT', 'Marketing']}

df = pd.DataFrame(data)

# Display the original DataFrame

print("Current DataFrame:")
print(df)

# Selecting columns

selected_columns = df[['Name', 'Salary']]
print("\nSelected Columns:")
print(selected_columns)

# 2) Selecting Rows Based on Condition

selected_rows = df[df['Age'] > 25]
print("\nSelected Rows Based on Condition (Age > 25):")
print(selected_rows)

# 3) Handling Missing Data

df.loc[2, 'Salary'] = np.nan  # Simulate a missing value in the 'Salary' column
df.fillna(df.Salary.mean(), inplace=True)  # Fill missing values with mean
print("\nDataFrame After Handling Missing Data:")
print(df)

# 4) Grouping and Aggregate data

grouped_data = df.groupby('Department')['Salary'].agg(['mean', 'sum'])
print("\nGrouped and Aggregated Data:")
print(grouped_data)

# 5) Merging Data frames

data2 = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
         'Bonus': [2000, 3000, 2500, 3500, 2800]}

df2 = pd.DataFrame(data2)

merged_df = pd.merge(df, df2, on='Name', how='left')
print("\nMerged DataFrames:")
print(merged_df)

# 6) Pivot Table

pivot_table = pd.pivot_table(df, values='Salary', index='Department', columns='Name', aggfunc=np.sum, fill_value=0)
print("\nPivot Table:")
print(pivot_table)

# 7) Time Series

date_rng = pd.date_range(start='2022-01-01', end='2022-01-05', freq='D')
time_series_data = {'Date': date_rng, 'Value': [10, 15, 20, 25, 30]}
time_series_df = pd.DataFrame(time_series_data)
print("\nTime Series DataFrame:")
print(time_series_df)
"""
# ------------------------------------------------------------------------------------------------------------
"""
# Appending DataFrames Vertically:
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

# Append DataFrames vertically using pd.concat()
result_vertical = pd.concat([df1, df2], axis=0)

print("DataFrame 1:")
print(df1)

print("\nDataFrame 2:")
print(df2)

print("\nAppended Vertically:")
print(result_vertical)
print("-----------------------------------------------------------------------------------------------")
"""


"""
# Appending DataFrames Horizontally:
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'C': [5, 6], 'D': [7, 8]})

result_horizontal = pd.concat([df1, df2], axis=1)

print("DataFrame 1:")
print(df1)

print("\nDataFrame 2:")
print(df2)

print("\nAppended Horizontally:")
print(result_horizontal)
print("-----------------------------------------------------------------------------------------------")

"""

"""
# Inner Merge of Two DataFrames:
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Age': [25, 30, 22]})

result_inner = pd.merge(df1, df2, on='ID', how='inner')

print("DataFrame 1:")
print(df1)

print("\nDataFrame 2:")
print(df2)

print("\nInner Merge:")
print(result_inner)
print("-----------------------------------------------------------------------------------------------")

"""

"""
# Left Outer Merge of DataFrames:
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Age': [25, 30, 22]})

# Left outer merge of DataFrames using pd.merge()
result_left_outer = pd.merge(df1, df2, on='ID', how='left')

print("DataFrame 1:")
print(df1)

print("\nDataFrame 2:")
print(df2)

print("\nLeft Outer Merge:")
print(result_left_outer)
print("-----------------------------------------------------------------------------------------------")

"""
"""

# Right Outer Merge of DataFrames:

df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Age': [25, 30, 22]})

# Right outer merge of DataFrames using pd.merge()
result_right_outer = pd.merge(df1, df2, on='ID', how='right')

print("DataFrame 1:")
print(df1)

print("\nDataFrame 2:")
print(df2)

print("\nRight Outer Merge:")
print(result_right_outer)
"""
