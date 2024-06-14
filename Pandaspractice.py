import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import sqlalchemy

# Creating a dataframe
df = pd.read_csv('Book1.csv')

# Maximum salary earned
max_age = df['Age'].max()
print(max_age)

# The Mean salary
mean_salary = df['Salary'].mean()
print(mean_salary)

# Print the statistics for the columns
print(df.describe())

# Print Salaries greater than 150000
print(df[df.Salary > 150000])

# Print salaries that are equal to the maximum salary
print(df[df.Salary == df.Salary.max()])

# Print salaries that are equal to the maximum salary
print(df[['Days Worked', 'Name']][df.Salary == df.Salary.max()])

# Prints all data from the rows and column from a specified index
print(df.loc[1])

# -----------------------------Different ways in Creating Dataframes----------------------------------------------------------------------
df = pd.read_csv("Book1.csv")  # Reading a csv file into the dataframe

df = pd.read_excel("Book1.xlsx", "Sheet1")  # Reading a excel file into the dataframe

data = {'day': ["1/1/2024", "2/2/2024", "3/3/2023"], 'temperature': [32, 35, 38], 'wind speed': [6, 7, 2],
        'event': ['Rain', 'Sunny', 'Snow']}
df = pd.DataFrame(data)  # Creating a Dictionary to be passed through the DataFrame() Function

# Creating DataFrames using Tuples
sample_data = [("1/1/2024", 32, 6, 'Rain'), ("2/2/2024", 35, 7, 'Sunny'), ("3/3/2024", 38, 2, 'Snow')]
df = pd.DataFrame(sample_data, columns=["Day", "Temperature", "Wind Speed", "Event"])

# Creating DataFrames using a list of dictionaries
sample_data = [{"Day": "1/1/2024", "Temperature": 32, "Windspeed": 6, "Event": "Rain"},
               {"Day": "2/2/2024", "Temperature": 35, "Windspeed": 7, "Event": "Sunny"},
               {"Day": "3/3/2024", "Temperature": 38, "Windspeed": 2, "Event": "Snow"}]
df = pd.DataFrame(sample_data)

# ------------------------------------Read/Write into CSV/Excel files------------------------------------------
df = pd.read_csv("Book1.csv", skiprows=1)  # Skip the first row in the csv file to the second row
df = pd.read_csv("Book1.csv", header=1)  # Does the samething as skiprows

df = pd.read_csv("Book1.csv", nrows=2)  # This limits the amount of rows to be shown/printed

df = pd.read_csv("Book1.csv", na_values=["Hello", "Hi"])
df = pd.read_csv("Book1.csv", na_values={"Name": "No name", "Age": "No age present"})
# In the above line of code you can use dictionaries, and lists to fill in missing data within the
# dataframe. Would have to do further research as to why there is a error above.

df.to_csv('new.csv', index=False, columns=["A", "B"])


# You can write to a new csv file and add columns to it

def convert_name_cell(cell):  # Defining a function to clean up the value in a cell
    if cell == "n.a.":
        return "Earl"
    return cell


# This could be done to replace other missing or null data within other columns within the excel file

df = pd.read_excel("Book1.xlsx", "Sheet1", converters={'Name': convert_name_cell(df['Name'])})
# Reading a Excel file into the dataframe also we are using a function to clean up the cells within a excel
# file by reading in all the names from the "Name: column

df.to_excel("new.xlsx", sheet_name="Sheet1", index=False, startcol=1, startrow=1)
# Writing to a new excel file, with the name of the sheet, also removing the index and starting at col 1
# and row 1

# ----------------Handle Missing Data: fillna, dropna, interpolate-----------------------------------------------
df = pd.read_csv("book1.csv", parse_dates=["date"])
# This would convert the column with dates in it, to actual 'date' datatype and not string

df.set_index("date", inplace=True)  # This line of code would make a certain column the index

df.fillna(0)  # This would fill all the cells with 'n.a' or 'na' with zero, you can also add more things to it
df.fillna({"name": "johnson", "age": "25", "department": "No department"})
# A dictionary can be used as well to fill in missing values with certain columns

df.fillna(method="ffill")  # This line of code would copy the previous data forward into a new cell
df.fillna(method="bfill")  # This line of code would copy the forward data cell
# and copy it into the previous data cell position

# ----------------------------Handle Missing Data: replace function-------------------------------------------

new_df = df.replace(9999, np.NAN)  # The standard way on how to use the replace function
new_df = df.replace({"name": "dx", "age": 0, "deparmtnet": 0}, np.NAN)
# Using a dictionary to replace values within each column with the names of the keys as the column names
new_df = df.replace({9999: np.NAN, "fourteen": 14})
# You can put values to replace values instead of having to put in the column games
new_df = df.replace({"temperature": ['A-Za-z'], "windspeed": ['A-Za-z']}, '', regex=True)
# When you want to get rid of the string that follows after a digit/numeral within a column or cell
new_df = df.replace(["poor", "average", "good", "excellent"], [1, 2, 3, 4])
# You can replace a list with a list -
# The above line of code is showing that whenever a value pops up it replaces it with another value
# E.g whenever 'poor' pops up it replaces it with the value 1
# -------------------------------------Group by function-------------------------------------------------------
g = df.groupby('city')  # column name - Standard group by function
for city, city_df in g:
    print(city)
    print(city_df)
    # This statement would print out the name of the city first then the corresponding data from each city
g.max()  # This would give us the 'Max' data correspondents for each city
g.mean()  # This would give us the 'Mean' data correspondents for each city
g.describe()  # This would give all the analytics for the 'grouped' cities

g.plot.scatter()
g.plot()  # This would create a graph of the grouped data for cities

# -----------------------------Concat DataFrames------------------------------------------------------
world_weather = pd.DataFrame(
    {"City": ["Paris", "London", "Brussels"], "Temperature": [67, 89, 78], "Humidity": [56, 70, 50]})
US_weather = pd.DataFrame(
    {"City": ["Atlanta", "Buffalo", "Dallas"], "Temperature": [78, 80, 70], "Humidity": [50, 40, 59]})

df = pd.concat([world_weather, US_weather], ignore_index=True)
# Joins two dataframes together also this would output a dataframe with a continuous index

df = pd.concat([world_weather, US_weather], keys=["World", "USA"])
# This would print the same dataframe however the respective data for 'World' and 'USA' would be labelled

df = pd.concat([world_weather, US_weather], axis=1)
# By adding 'axis=1' it will concat the dataframe as a columm next to the first dataframe

s = pd.Series(["Humid", "Dry", "Wet"], name="Event")
# Creating a series that stores weather conditions with the title as 'Event'

df = pd.concat([US_weather, s], axis=1)  #
# Concating the series with the Dataframe 'US_Weather' to create another dataframe

# ---------------------------------Merge DataFrames-----------------------------------------------------------
city_temperature = pd.DataFrame(
    {"City": ["Paris", "London", "Brussels"], "Temperature": [67, 89, 78]})

city_Humidity = pd.DataFrame(
    {"City": ["Paris", "London", "Brussels"], "Humidity": [56, 70, 50]})

new_dff = pd.merge(city_Humidity, city_temperature, on="City", how='inner')
# The merge functuon is like the join in sql - You have inner, outer, left and right

# ----------------------------------Pivot/Pivot Table-------------------------------------------------------------
new_df = pd.read_csv("Book1.csv")
new_df = pd.pivot(index="Name", columns=["Salary", "Age"], values="Days Worked")
# A pivot displays the dataframe based on the conditions you have set above
# The values method displays only the values that are within that specified column

new_df = pd.pivot_table(index="Name", columns="Salary", aggfunc="sum")
# Pivot table are used to aggregate and summarize data within a dataframe
# You can use 'aggfunc' to define what specific aggregate function you want to use

new_df = pd.pivot_table(index=pd.Grouper(freq="", key=""), columns="")
# You can use this grouper function to aggregate data
# you can learn more about this within the grouper documentation online


# ---------------------------------DateTime Index/Resample---------------------------------------------------
df = pd.read_csv("Book1.csv", parse_dates=["Date"], index_col="Date")
# Here we convert the dates within the dataframe to actual datetime using 'parse_dates'
# and made it the index use the 'index_col'

df.resample('M').mean() # 'S', 'H', 'D', 'W', 'M'
# This line of code allows us to change the frequency of the data being processed
# By resampling which are changing the rate at whic in terms of time we are processing the data
# Whether by seconds, hours, days, weeks, months etc....

# ----------------------------Read/Write Data from Database(read_sql/to_sql)---------------------------------
engine = sqlalchemy.create_engine('mysql+pymysql://root:@localhost:3306')

# --------------------------------Vectorized Strings----------------------------------------------------------
# Create a DataFrame with a column of strings
data = {'Name': ['Alice', 'Bob', 'Charlie']}
df = pd.DataFrame(data)

# Convert all names to uppercase
df['Name_Upper'] = df['Name'].str.upper()


# Common string operations include `str.upper()`, `str.lower()`,
# `str.len()` (length), `str.contains()`, and more.

# ---------------------------------Scatter Plot/Matplotlib--------------------------------------------------
# A scatter plot is a type of data visualization that displays individual data points on a
# two-dimensional graph. Each point on the graph represents the values of two variables,
# one plotted along the x-axis and the other along the y-axis. Scatter plots are useful
# for visually examining the relationship between two continuous variables and identifying patterns,
# trends, or correlations in the data.


data = {'Age': [25, 30, 22, 35, 28],
        'Salary': [50000, 60000, 45000, 70000, 55000]}

df = pd.DataFrame(data)

df.plot.scatter(x='Age', y='Salary', title='Scatter Plot: Age vs Salary')

plt.show()

# ---------Additional Features in Scatter Plot:
data = {'Age': [25, 30, 22, 35, 28],
        'Salary': [50000, 60000, 45000, 70000, 55000],
        'Experience': [3, 5, 2, 8, 4]}

df = pd.DataFrame(data)

df.plot.scatter(x='Age', y='Salary', c='Experience', colormap='viridis',
                s=df['Experience'] * 10, alpha=0.8, edgecolors='w',
                title='Scatter Plot: Age vs Salary with Experience')

plt.show()

# -------------------------------------Plotly-----------------------------------------------------------------
# Plotly is a data visualization library that allows users to create interactive and
# visually appealing plots and charts. It provides a high-level interface for creating
# a wide range of charts, including line charts, scatter plots, bar charts, and more.
# Plotly visualizations are interactive, meaning users can zoom, pan, hover over data points
# for details, and more, directly in the generated plots.


data = {'Age': [25, 30, 22, 35, 28],
        'Salary': [50000, 60000, 45000, 70000, 55000]}

df = pd.DataFrame(data)
df["Age"]
fig = px.scatter(df, x='Age', y='Salary', title='Scatter Plot: Age vs Salary')
fig.show()

# Additional feature of plotly
data = {'Age': [25, 30, 22, 35, 28],
        'Salary': [50000, 60000, 45000, 70000, 55000],
        'Experience': [3, 5, 2, 8, 4],
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily']}

df = pd.DataFrame(data)

# Scatter plot with additional features
fig = px.scatter(df, x='Age', y='Salary', color='Experience', size='Experience',
                 hover_data=['Name'], title='Scatter Plot: Age vs Salary with Experience')
fig.show()
