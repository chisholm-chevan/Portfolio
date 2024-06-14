import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('sales.csv')

# Line Plot
plt.figure(figsize=(12, 10))
plt.plot(df['Months'], df['Sales'], marker='o', label='Sales')
plt.plot(df['Months'], df['Expenses'], marker='o', label='Expenses')

plt.title('Monthly Sales and Expenses Trend')
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.legend()
plt.grid(True)
plt.show()


# Bar Chart
plt.figure(figsize=(12, 10))
plt.bar(df['Months'], df['Sales'], color='blue', label='Sales')
plt.bar(df['Months'], df['Expenses'], color='orange', label='Expenses')

plt.title('Monthly Sales and Expenses Comparison')
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.legend()
plt.show()


# Scatter Plot
plt.figure(figsize=(12, 10))
plt.scatter(df['Sales'], df['Expenses'], color='green', marker='o')

plt.title('Relationship between Sales and Expenses')
plt.xlabel('Sales')
plt.ylabel('Expenses')
plt.show()

# Histogram
plt.figure(figsize=(12, 10))
plt.hist(df['Sales'], color='purple', edgecolor='black')

plt.title('Distribution of Monthly Sales')
plt.xlabel('Sales ($)')
plt.ylabel('Frequency')
plt.show()

# Pie Chart
plt.figure(figsize=(12, 12))
plt.pie(df['Sales'], labels=df['Months'], autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)

plt.title('Proportion of Total Sales by Month')
plt.show()

# Custom Visualization - Stacked Bar Chart
plt.figure(figsize=(12, 10))
plt.bar(df['Months'], df['Sales'], color='blue', label='Sales')
plt.bar(df['Months'], df['Expenses'], bottom=df['Sales'], color='orange', label='Expenses')

plt.title('Monthly Sales and Expenses (Stacked)')
plt.xlabel('Months')
plt.ylabel('Amount ($)')
plt.legend()
plt.show()
"""

# -------------------------Case Study----------------------------------
"""
xcel_ = pd.read_excel('matplot/newfile.xlsx','Sheet1')

df = pd.DataFrame(xcel_)
plt.figure(figsize=(14, 8))

plt.plot(df['Month'], df['Total_Expenses_per_month'], marker='o', color='b')
plt.title('Total Trend in Monthly Expenses ')
plt.xlabel('Month')
plt.ylabel('Monthly Expense Amount')

plt.grid(True)
plt.show()

# ----------------------------------------------------

xcel_ = pd.read_excel('matplot/bar.xlsx','Sheet1')

df = pd.DataFrame(xcel_)
plt.figure(figsize=(12, 8))
plt.bar(df['Category'], df['Total_Expense_per_category'], color="blue")
plt.title('Total Expense for each Category')
plt.xlabel('Category')
plt.ylabel('Expense Amount')
plt.legend(title='Category', bbox_to_anchor=(1, 1))
plt.show()


# ---------------------------------------------------------------
xcel_ = pd.read_excel('matplot/pie.xlsx','Sheet1')

df = pd.DataFrame(xcel_)
plt.figure(figsize=(10, 10))
plt.pie(df['Percentage'],
        labels=df['Category'].unique(),
        autopct='%1.1f%%',
        startangle=90,
        colors=sns.color_palette('pastel'))

plt.title('Category-wise Distribution of Expenses')
plt.show()


# ---------------------------------------------------------------------------------------
xcel_ = pd.read_excel('matplot/pie.xlsx','Sheet1')

df = pd.DataFrame(xcel_)

top_categories = df.groupby('Category')['Total_Expense_per_category'].sum().nlargest(3)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_categories.values, y=top_categories.index, palette='viridis')
plt.title('Top 3 High-Expense Categories')
plt.xlabel('Expense Amount')
plt.ylabel('Category')

plt.show()



