import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 12)

connection_url = 'mysql://root:Generalboy$1@localhost/case_study'
engine = create_engine(connection_url)

# 2. Data Cleaning and Preprocessing:
# Utilize Pandas to clean and preprocess the data, addressing issues such as missing values,
# duplicate entries, and data inconsistencies.
# Perform data transformations and feature engineering to prepare the dataset for analysis.

"""
# A query to select a values from a select table
query = 'select * from Products' # Just change the name of table to produce the records
df = pd.read_sql_query(query, engine)
print(df)
print('\n')

# A query to check if there are null values in a column
query1 = "select * from Products where Product_ID is null"  # Just change the name of table to produce the records
df1 = pd.read_sql_query(query1, engine)
print(df1)
print('\n')

# A query to check for duplicates within a specified column in a table
query2 = ("SELECT Customer_ID, COUNT(*) as count FROM sales GROUP BY Customer_ID HAVING COUNT(*) > 1;")
df2 = pd.read_sql_query(query2, engine)
print(df2)
"""

"""
# Display the first few rows of the DataFrame
query = "select * from Customers Limit 3"
df = pd.read_sql(query,engine)
print(df)
print('\n')
query = "select * from Stores Limit 3"
df = pd.read_sql(query,engine)
print(df)
print('\n')
query = "select * from Sales Limit 3"
df = pd.read_sql(query,engine)
print(df)
print('\n')
query = "select * from Products Limit 3"
df = pd.read_sql(query,engine)
print(df)
"""

"""
# Get summary statistics of numerical columns
query = "select * from Customers"
df = pd.read_sql(query,engine)
print(df.describe())
print('\n')

query = "select * from Stores"
df = pd.read_sql(query,engine)
print(df.describe())
print('\n')

query = "select * from Sales"
df = pd.read_sql(query,engine)
print(df.describe())
print('\n')

query = "select * from Products"
df = pd.read_sql(query,engine)
print(df.describe())
"""



"""
# Check the data types of each column
query = "select * from Customers"
df = pd.read_sql(query,engine)
print(df.dtypes)
print("-----------------------------------")
print('\n')

query = "select * from Stores"
df = pd.read_sql(query,engine)
print(df.dtypes)
print("-----------------------------------")
print('\n')

query = "select * from Sales"
df = pd.read_sql(query,engine)
print(df.dtypes)
print("-----------------------------------")
print('\n')

query = "select * from Products"
df = pd.read_sql(query,engine)
print(df.dtypes)
"""
"""
# Check the number of rows and columns in the DataFrame
query = "select * from Customers"
df = pd.read_sql(query,engine)
print(df.shape)
print("-----------------------------------")

query = "select * from Stores"
df = pd.read_sql(query,engine)
print(df.shape)
print("-----------------------------------")

query = "select * from Sales"
df = pd.read_sql(query,engine)
print(df.shape)
print("-----------------------------------")

query = "select * from Products"
df = pd.read_sql(query,engine)
print(df.shape)
"""

# 3. Exploratory Data Analysis (EDA):
# Conduct exploratory data analysis using Pandas to uncover patterns, trends, and relationships within the data.
# Generate summary statistics, and descriptive insights to understand sales patterns across
# different regions, products, and customer segments.

# Group the data by region and calculate total sales
"""
query = ("select Stores.store_ID,Stores.Store_Location,Sales.Sales_ID,Sales.Sale_Cost "
         "from Stores "
         "Join Sales "
         "on Stores.Store_ID = Sales.Store_ID;")
df = pd.read_sql(query, engine)
sql = df.groupby('Store_Location').agg(Total_Sales=('Sale_Cost', 'sum')).reset_index()
print(sql)
"""

"""
# Group the data by product category and calculate average sales

query = ("select Products.Product_ID,Products.Product,Products.Car_Item_class,Sales.Sales_ID,Sales.Sale_Cost"
         " from Products "
         "Join Sales "
         "on Products.Product_ID = Sales.Product_ID;")
df = pd.read_sql(query,engine)
sql = df.groupby(['Product','Car_Item_class']).agg(Avg_Sales=('Sale_Cost','mean')).reset_index()
print(sql)

"""

"""
# Group the data by customer segment and calculate total sales

query = ("select Customers.Customer_ID,Customers.Fname,Customers.Lname,Sales.Sales_ID,Sales.Sale_Cost "
         "from Customers "
         "Join Sales "
         "on Customers.Customer_ID = Sales.Customer_ID;")
df = pd.read_sql(query, engine)
sql = df.groupby(['Customer_ID', 'Fname', 'Lname']).agg(Total_Sales=('Sale_Cost', 'sum')).reset_index()
print(sql)

"""

# 4. Sales Performance Analysis:
# - Use SQL queries and Pandas operations to analyze sales performance metrics such as total
# revenue, average transaction value, and sales growth over time.
# - Identify top-selling products, best-performing stores, and key factors driving sales variations.


# Calculate total revenue
"""
query = "select * from Sales;"
df = pd.read_sql(query,engine)
sql = df['sale_cost'].sum()
print("The total sales amount is:",sql)
"""
"""
# Calculate average transaction value
query = "select * from Sales;"
df = pd.read_sql(query,engine)
average_trans_value = df['sale_cost'].mean()
print("The average sale amount:",average_trans_value)
"""

"""
# Identify sales growth over time
query = "select * from Sales;"
df = pd.read_sql(query,engine)
df['sale_date'] = pd.to_datetime(df['sale_date'])
df.set_index('sale_date', inplace=True)
monthly_revenue = df.resample('ME')['sale_cost'].sum()
print("The monthly revenue is:",monthly_revenue)
"""

"""
# Identify top-selling products
query = ("select Products.Product_ID,Products.Product,Products.Car_Item_class,Sales.Sales_ID,Sales.Sale_Cost from "
         "Products "
         "Join Sales "
         "on Products.Product_ID = Sales.Product_ID;")
df = pd.read_sql(query,engine)
sql = df.groupby(['Product_ID','Product','Car_Item_class']).agg(Top_Sell_Amount=('Sale_Cost', 'sum'))
sql1 = sql.sort_values('Top_Sell_Amount', ascending=False)
print(sql1)
"""

"""
# Identify best-performing stores
query = ("select Stores.Store_ID,Stores.Store_Location,Stores.Store_Name,Sales.Sales_ID,Sales.Sale_Cost "
         "from Stores "
         "Join Sales "
         "on Stores.Store_ID = Sales.Store_ID;")
df = pd.read_sql(query, engine)
sql = df.groupby(['Store_ID', 'Store_Name']).agg(Top_Perform_Stores_Amount=('Sale_Cost', 'sum'))
sql1 = sql.sort_values('Top_Perform_Stores_Amount', ascending=False)
print(sql1)
"""

"""
# 5. Customer Segmentation: Apply segmentation techniques using Pandas to categorize customers based on their
# purchasing behavior, demographics, or other relevant attributes. Analyze the characteristics
# and preferences of different customer segments to tailor marketing strategies and promotions accordingly.

query = ( "SELECT C.Customer_ID,C.Fname,C.Lname,ST.Store_Name,ST.Store_Location,S.Sales_ID, S.sale_cost,S.sale_date, "
          "S.Store_ID," "P.Product_ID,P.Product,P.Car_Item_class " "FROM Sales AS S " "INNER JOIN Customers C " "Using (Customer_ID) " "INNER JOIN Products P " "USING (Product_ID) " "INNER JOIN Stores ST " "USING (Store_ID);")
df = pd.read_sql(query,engine)
print(df)

# For Customer one - Dave Bernard he buys tires frequently in Jamaica. Probably have to do with the bad roads in Jamaica
# For Customer two - There is only a one time instance of her buying tires in Jamaica - No patterns here
# For Customer three - There is only a one time instance of her buying spoilers in the Bahamas - No patterns here
# For Customer four - Luke lives in Cayman's and there's only one instance of him buying an engine
# For Customer Five - There is only a one time instance of her buying tires in Jamaica - No patterns here
# For Customer six - Diogo bought an engine oil. This is the only occurrence.
# For Customer seven - Ashely only have on occurrence of buying break fluid.
# For Customer eight - John lives in the Dominican Republic and only have bought break fluid one time.
# For Customer nine - Vic lives in the Dominican Republic and bought only one transmission box
# For Customer ten - Tom lives in Trinidad  bought tires. This is the only occurrence.


# 6. Sales Forecasting:
# Implement time-series forecasting models using Pandas and statistical techniques to predict future sales trends.
# Evaluate the accuracy of the forecasting models and adjust parameters as needed to improve predictions.

query = "SELECT * FROM Sales"
df = pd.read_sql(query, engine)

# Convert the 'sales date' column to datetime format
df['sale_date'] = pd.to_datetime(df['sale_date'])

# Set the 'date' column as the index
df.set_index('sale_date', inplace=True)

# Resample the data to aggregate sales on a monthly basis
monthly_sales = df['sale_cost'].resample('ME').sum()

# Calculate simple moving average (SMA) for 3 months
sma_3 = monthly_sales.rolling(window=3).mean()

# Forecast future sales using the last value of SMA
forecast_period = 12  # forecast for the next 12 months
last_sma_value = sma_3.iloc[-1]
forecast_values = pd.Series([last_sma_value] * forecast_period, index=pd.date_range(start=monthly_sales.index[-1], periods=forecast_period, freq='ME'))

# Evaluate the accuracy of the forecasts
actual_sales = monthly_sales[-forecast_period:]
forecast_errors = actual_sales - forecast_values[:len(actual_sales)]

mean_absolute_error = forecast_errors.abs().mean()
mean_squared_error = (forecast_errors ** 2).mean()

print(actual_sales)

print("Mean Absolute Error (MAE):", mean_absolute_error)
# The Mean Absolute Error (MAE) in sales forecasting
# is a measure of the average magnitude of errors between predicted and actual sales values.
# It is calculated by finding the average absolute difference between each predicted sales value
# and the corresponding actual sales value. Basically the difference between your predicted sales and the actual sales
# is the mean absolute error
print("Mean Squared Error (MSE):", mean_squared_error)
# The Mean Squared Error (MSE) in sales forecasting is another measure of the average magnitude of errors
# between predicted and actual sales values, but it gives more weight to larger errors.
# It is calculated by finding the average of the squared differences between each predicted sales value
# and the corresponding actual sales value.

# Plotting actual vs forecasted sales
plt.figure(figsize=(10, 6))
plt.plot(monthly_sales.index, monthly_sales, label='Actual Sales')
plt.plot(forecast_values.index, forecast_values, label='Forecasted Sales', linestyle='--')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Actual vs Forecasted Sales')
plt.legend()
plt.show()

# 7. Inventory Optimization:
# Use historical sales data and inventory information to optimize inventory levels, minimize
# stockouts, and reduce excess inventory.
# Develop strategies for inventory replenishment and allocation based on demand forecasting
# and sales projections.

# Query the joined sales and inventory data from the database
query = ("SELECT Sales.sale_date, Sales.Store_ID, Sales.Product_ID, Sales.sale_cost,Products.Product, "
         "Products.Car_Item_class,Products.product_cost "
         "FROM Sales "
         "JOIN Products "
         "ON Sales.Product_ID = Products.Product_ID; ")
df = pd.read_sql(query, engine)

# Convert the 'date' column to datetime format
df['sale_date'] = pd.to_datetime(df['sale_date'])

# Group by store and product, then calculate average daily sales and average inventory level
summary_df = df.groupby(['Store_ID', 'Product_ID']).agg(avg_daily_sales=('sale_cost', 'mean'),
                                                        avg_inventory_level=('product_cost', 'mean')
                                                        ).reset_index()

# Calculate inventory turnover rate (average daily sales / average inventory level)
summary_df['inventory_turnover_rate'] = summary_df['avg_daily_sales'] / summary_df['avg_inventory_level']

# Identify products with low turnover rates indicating excess inventory
low_turnover_products = summary_df[summary_df['inventory_turnover_rate'] < 2.5]

# Implement strategies for inventory management based on turnover rates
for index, row in low_turnover_products.iterrows():
    Store_ID = row['Store_ID']
    Product_ID = row['Product_ID']
    current_inventory = row['avg_inventory_level']
    forecasted_sales = row['avg_daily_sales'] * 30  # Forecasting sales for the next month

    # Example strategy: Adjust inventory levels based on forecasted sales
    if forecasted_sales < current_inventory:
        print(f"Consider reducing inventory of product {Product_ID} in store {Store_ID}.")
    elif forecasted_sales > current_inventory:
        print(f"Consider increasing inventory of product {Product_ID} in store {Store_ID}.")
    else:
        print(f"Maintain current inventory levels of product {Product_ID} in store {Store_ID}.")

# 8. Insights and Recommendations:
# Summarize key findings and insights from the analysis, highlighting actionable
# recommendations for improving business performance.
# Present the analysis results visually through interactive dashboards or reports, using tools like
# Matplotlib, Seaborn, or Plotly.


# Chart showing the monthly revenue
query = "select * from Sales;"
df = pd.read_sql(query,engine)
df['sale_date'] = pd.to_datetime(df['sale_date'])
df.set_index('sale_date', inplace=True)
monthly_revenue = df.resample('ME')['sale_cost'].sum()
print("The monthly revenue is:",monthly_revenue)

plt.figure(figsize=(10, 6))
plt.plot(monthly_revenue.index, monthly_revenue.values)
plt.title('Sales Growth Over Time')
plt.xlabel('Year-Month')
plt.ylabel('Monthly Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Chart showing the total amount per store
query = ("select Products.Product_ID,Products.Product,Products.Car_Item_class,Sales.Sales_ID,Sales.Sale_Cost from "
         "Products "
         "Join Sales "
         "on Products.Product_ID = Sales.Product_ID;")
df = pd.read_sql(query,engine)
sql = df.groupby(['Product_ID','Product','Car_Item_class']).agg(Top_Sell_Amount=('Sale_Cost', 'sum')).reset_index()
sql = sql.sort_values(by='Top_Sell_Amount')
print(sql)

plt.figure(figsize=(14, 6))
plt.scatter(sql['Product'], sql['Top_Sell_Amount'])
plt.title('Graph Showing The Amount Sold Per Products')
plt.xlabel('Top_Selling_Products')
plt.ylabel('Product Amounts')
plt.tight_layout()
plt.show()



# Chart Showing the Total Amount per Product
# Here we can see the best performing product and the worst performing product and their amounts
query = ("SELECT Sales.sale_cost, Products.Product_ID,Products.Product "
         "FROM Sales   "
         "JOIN Products  "
         "ON Sales.Product_ID = Products.Product_ID;")
df = pd.read_sql(query, engine)
sql = df.groupby(['Product_ID', 'Product']).agg(Total_Amount=('sale_cost', 'sum'))

print(sql)

plt.figure(figsize=(10, 6))
plt.bar(sql.index.get_level_values('Product'), sql['Total_Amount'])
plt.title('Total Amount of Each Product')
plt.xlabel('Product')
plt.ylabel('Total Amount')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Chart showing sales growth over time
query = "select * from Sales;"
df = pd.read_sql(query,engine)
df['sale_date'] = pd.to_datetime(df['sale_date'])
df.set_index('sale_date', inplace=True)
sql1 = df.groupby('sale_date').agg(Total_Growth_Overtime=('sale_cost','sum'))
print(sql1)

plt.figure(figsize=(10, 6))
plt.plot(sql1.index,sql1['Total_Growth_Overtime'], )
plt.title('Chart Showing Sales growth over time')
plt.xlabel('Months')
plt.ylabel('Total Amount')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Chart showing the best performing stores
query = ("select Stores.Store_ID,Stores.Store_Location,Stores.Store_Name,Sales.Sales_ID,Sales.Sale_Cost "
         "from Stores "
         "Join Sales "
         "on Stores.Store_ID = Sales.Store_ID;")
df = pd.read_sql(query, engine)
sql = df.groupby(['Store_ID', 'Store_Name']).agg(Top_Perform_Stores_Amount=('Sale_Cost', 'sum')).reset_index()
print(sql)

plt.figure(figsize=(10, 6))
plt.bar(sql['Store_Name'], sql['Top_Perform_Stores_Amount'])
plt.title('Chart showing the Top Performing Stores')
plt.xlabel('Store Name')
plt.ylabel('Total Amount')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

"""
# Group the data by product category and calculate average sales
query = ("select Products.Product_ID,Products.Product,Products.Car_Item_class,Sales.Sales_ID,Sales.Sale_Cost"
         " from Products "
         "Join Sales "
         "on Products.Product_ID = Sales.Product_ID;")
df = pd.read_sql(query,engine)
sql = df.groupby(['Product','Car_Item_class']).agg(Avg_Sales=('Sale_Cost','mean')).reset_index()
print(sql)

plt.figure(figsize=(10, 6))
plt.bar(sql['Car_Item_class'], sql['Avg_Sales'])
plt.title('Chart showing the average revenue for each brand ')
plt.xlabel('Brand Name')
plt.ylabel('Average Revenue')
plt.tight_layout()
plt.show() 



