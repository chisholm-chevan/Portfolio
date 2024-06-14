import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

# SQL TRANSLATION

connection_url = 'mysql://root:Generalboy$1@localhost/sql_translate'
engine = create_engine(connection_url)

query = "select * from employees;"
query2 = "select * from orders"
df = pd.read_sql(query, engine)
df1 = pd.read_sql(query2, engine)
# new_data = df[df.groupby('Customer_ID')['sale_cost']].sum()
# print(new_data)


"""
# 1. Question: How would you achieve the equivalent result using Pandas DataFrame?
# SQL Query: SELECT * FROM employees;
sql = df.head()
print(sql)


# 2. Question: Translate this SQL query into Pandas DataFrame operations.
# SQL Query:SELECT employee_id, first_name, last_name FROM employees WHERE department_id= 10;

sql = df[df['DepartmentID'] == 22001]
print(sql)


# 3. Question: Using Pandas, how can you calculate the average and maximum salary for
# employees in department 20?

# SQL Query:SELECT AVG(salary) as avg_salary, MAX(salary) as max_salary FROM employees
# WHERE department_id = 20;
filtered_df = df[df['DepartmentID'] == 22001]

# Calculate average and maximum salary
avg_salary = filtered_df['Salary'].mean()
print("Average Salary: ",avg_salary)
max_salary = filtered_df['Salary'].max()
print("Max Salary: ",max_salary)

# 4. Question: Write the equivalent Pandas code to obtain the count of employees in each department.
# SQL Query:
# SELECT department_id, COUNT(employee_id) as num_employees FROM employees
# GROUP BY department_id;

sql = df.groupby('DepartmentID').agg(num_employees=('EmployeeID', 'count')).reset_index()
print(sql)


# 5. Question: Translate the given SQL query to Pandas and filter orders for customer 'C001' with
# an order date on or after'2022-01-01'.
# SQL Query:
# SELECT * FROM orders WHERE order_date >= '2022-01-01' AND customer_id = 1;


df1['OrderDate'] = pd.to_datetime(df1['OrderDate'])

sql = df1[(df1['OrderDate'] >= '2022-01-01') & (df1['CustomerID'] == 1)]

print(sql)

# 6. Question: Convert this SQL query to Pandas code, grouping orders by customer and filtering those with a total amount spent greater than 1000.
# SQL Query:
# SELECT customer_id, SUM(order_amount) as total_spent FROM orders GROUP BY
# customer_id HAVING total_spent > 1000;

sql1 = df1.groupby('CustomerID').agg(total_spent=('OrderAmount', 'sum')).reset_index()

new = sql1[sql1['total_spent'] > 1000]

print(new)

# 7. Question: Achieve the same sorting in Pandas, ordering employees first by department_id and
# then by hire_date in descending order.
# SQL Query:
# SELECT * FROM employees ORDER BY department_id, hire_date DESC;

sql = df.sort_values(by=['DepartmentID', 'HireDate'], ascending=[True,False])
#sql1 = sql['EmployeeID']
print(sql)

# 8. Question: How would you retrieve unique job titles from the employees DataFrame in
# Pandas?
# SQL Query:
# SELECT DISTINCT job_title FROM employees;

sql = df['JobTitle'].unique()
print(sql)

# 9. Question: Translate the SQL query to Pandas code, filtering employees with last names
# starting with 'S'
# SQL Query:
# SELECT * FROM employees WHERE last_name LIKE 'S%';

sql = df[df['LastName'].str.startswith('S')]
print(sql)

"""
"""
# 10. Question : Convert the SQL query to Pandas, calculating the average salary for each
# department and filtering only those with an average salary greater than 50000.
# SQL Query:
# SELECT AVG(salary) as avg_salary, department_id FROM employees GROUP BY
# department_id HAVING avg_salary > 50000;

sql = df.groupby('DepartmentID').agg(avg_salary=('Salary','mean')).reset_index()

new = sql[sql['avg_salary'] > 50000]
print(new)

"""


