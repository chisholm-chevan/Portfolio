import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


"""
# Creating the original DataFrame
data = {'A': [1, 2, 3, 4, 5], 'B': ['a', 'b', 'c', 'd', 'e']}
df = pd.DataFrame(data)

# Shifting values by one position along the rows
df_shifted = df.shift(1)

# Displaying both the original and shifted DataFrames
print("Original DataFrame:")
print(df)

print("\nShifted DataFrame:")
print(df_shifted)
"""

"""
# Create a DataFrame with numerical and categorical columns
data = {'Numeric_Column': np.random.randn(100),
        'Another_Numeric_Column': np.random.randint(1, 100, 100),
        'Categorical_Column': np.random.choice(['A', 'B', 'C'], 100)}

df = pd.DataFrame(data)
print(df.head())
print(df.describe())
"""



"""
# Create a DataFrame with a column named 'Date' containing datetime values
date_rng = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
data = {'Date': date_rng, 'Numeric_Column': np.random.randn(len(date_rng))}
df = pd.DataFrame(data)

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Set the 'Date' column as the index
df.set_index('Date', inplace=True)

# Resample the time series data, taking monthly mean
df_resampled = df.resample('M').mean()

# Display the original DataFrame with datetime index
print("Original DataFrame:")
print(df.head())

# Display the resampled DataFrame
print("\nResampled DataFrame:")
print(df_resampled.head())
"""

# Create a DataFrame with 'Category' and 'Value' columns
data = {'Category': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
        'Value': [10, 15, 20, 25, 30, 35, 40, 45]}

df = pd.DataFrame(data)

# Group the data by 'Category' and calculate the mean of 'Value' for each group
grouped_data = df.groupby('Category')['Value'].mean()

# Display the grouped data
print("Grouped Data:")
print(grouped_data)

# Visualize the information using a bar plot
grouped_data.plot(kind='bar', rot=0, color='skyblue')
plt.title('Mean Value for Each Category')
plt.xlabel('Category')
plt.ylabel('Mean Value')
plt.show()