import pandas as pd
import numpy as np
# data = [10, 20, 30, 40, 50]
# print(data)
# print(type(data))
# series = pd.Series(data)
# print(series)
# print(type(series))


# # Months in a year
# months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
# 'October', 'November', 'December']
# # Monthly sales data for a product (example data)
# sales_data = [12000, 13500, 14200, 12800, 14000, 15500, 16200, 15800, 16500,17800, 18500, 17200]
# # Create a Pandas Series with months as the index
# sales_series = pd.Series(sales_data, index=months, name='Monthly Sales (USD)')
# # Display the Series
# print(sales_series)

# list = [1,2,3,4,5]
# res = pd.Series(list, index=['a','b','c','d','e'],dtype='float',name="Series")
# print(res)

# data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
# 'Age': [25, 30, 35, 28],
# 'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
# # Create a DataFrame from a dictionary
# df = pd.DataFrame(data)
# print(df)



# data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
# 'Age': [25, 30, 35, 28]}
# df = pd.DataFrame(data)
# print("Before Adding Column")
# print(df)
# # Add a new column "City" with values
# df['City'] = ['New York', 'Los Angeles', 'Chicago', 'Houston']
# print("After Adding Column")
# print(df)



# # Create an initial DataFrame
# data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
# 'Age': [25, 30, 35, 28],
# 'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
# df = pd.DataFrame(data)
# # Display the initial DataFrame
# print("Initial DataFrame:")
# print(df)
# # Create data for the new columns
# new_columns = {
# 'Gender': ['Female', 'Male', 'Male', 'Male'],
# 'Grade': ['A', 'B', 'C', 'B']
# }
# # Add the new columns to the DataFrame
# df['Gender'] = new_columns['Gender']
# df['Grade'] = new_columns['Grade']
# print("DataFrame after adding column :")
# print(df)


# # Create an initial DataFrame
# data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
# 'Age': [25, 30, 35, 28],
# 'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
# df = pd.DataFrame(data)
# # Display the initial DataFrame
# print("Initial DataFrame:")
# print(df)
# # Create data for the new column
# new_column_value = ['Female', 'Male', 'Male', 'Male']
# # Define the name and index where you want to insert the new column
# new_column_name = 'Gender'
# insert_index = 1 # Insert as the second column (index 1)
# # Insert the new column at the specified location
# df.insert(insert_index, new_column_name, new_column_value)
# # Display the DataFrame with the new column
# print("\nDataFrame after adding the new column:")
# print(df)


# Create an initial DataFrame
# data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
# 'Age': [25, 30, 35, 28],
# 'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
# df = pd.DataFrame(data)
# # Display the initial DataFrame
# print("Initial DataFrame:")
# print(df)
# # Create data for the new row
# new_row = pd.DataFrame([{'Name': 'Eve', 'Age': 24, 'City': 'San Francisco'}])
# #now we are adding a row at the end of the DataFrame
# df = pd.concat([df, new_row], ignore_index=True)
# # Display the DataFrame with the new row
# print("\nDataFrame after adding a new row:")
# print(df)



# # Create an initial DataFrame
# data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
# 'Age': [25, 30, 35, 28],
# 'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
# df = pd.DataFrame(data)
# # Display the initial DataFrame
# print("Initial DataFrame:")
# print(df)
# # Create data for the new rows
# new_rows = pd.DataFrame([
# {'Name': 'Eve', 'Age': 24, 'City': 'San Francisco'},
# {'Name': 'Frank', 'Age': 32, 'City': 'Miami'},
# {'Name': 'Grace', 'Age': 29, 'City': 'Seattle'}
# ])
# df = pd.concat([df, new_rows], ignore_index=True)
# # Display the DataFrame with the new rows
# print("\nDataFrame after adding new rows:")
# print(df)



# # Create an initial DataFrame
# data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
# 'Age': [25, 30, 35, 28],
# 'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
# df = pd.DataFrame(data)
# # Display the initial DataFrame
# print("Initial DataFrame:")
# print(df)

# #create data for the new row
# new_row = {'Name': 'Eve','Age':24, 'City':'San Francisco'}

# df.loc[3] = new_row

# print(df)

# df = df.rename(columns = {'Name':'First Name'})

# print(df)

# df = df.rename(columns = {'First Name':'Full Name','Age': 'Student Age','City': 'Student Cty'})

# print(df)

# df.columns = df.columns.str.lower()
# print(df)

# print(df.loc[1])
# df.loc[1] = {'full name':"Sanjay"}
# print(df)

# df = df.loc[1:3, 'full name':"student city"]
# print(df)



# fruit_data = {"Fruit": ['Apple','Avacado','Banana','Strawberry','Grape'],"Color":
# ['Red','Green','Yellow','Pink','Green'],
# "Price": [45, 90, 65, 37, 49]
# }
# #Dataframe
# data = pd.DataFrame(fruit_data)
# print("Original Dataset")
# print(data)
# #Updating
# data.loc[data['Price'] >60, 'Remarks'] = 'Expensive'
# data.loc[data['Price'] <60, 'Remarks'] = 'Not Expensive'
# print("After Updating Values")
# print(data)


# data = {
# 'EmployeeID': [101, 102, 103, 104, 105],
# 'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
# 'Age': [28, 32, 29, 35, 26]
# }
# df = pd.DataFrame(data)

# print("Initial DataFrame:")
# print(df)

# df = df.loc[df['Name'] != 'Charlie']

# print("DataFrame after deleting the row for 'Charlie':")
# print(df)


# data = {
# 'EmployeeID': [101, 102, 103, 104, 105],
# 'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
# 'Age': [28, 32, 29, 35, 26],
# 'Photo': ['photo1.jpg', 'photo2.jpg', 'photo3.jpg', 'photo4.jpg', 'photo5.jpg']
# }
# df = pd.DataFrame(data)

# print("Initial DataFrame:")
# print(df)

# df = df.drop('Photo', axis=1)

# print("\nDataFrame after deleting the 'Photo' column:")
# print(df)

# data = {
#     'Name':['Jay','Anuj','Abhay','Raj'],
#     'Age': [23,23,26,24],
#     'Address':['Delhi','Mumbai','Goa','shimla'],
#     'Qualification':['Msc','MA','MCA','Bteck']
# }

# df = pd.DataFrame(data)
# print(df[['Name','Qualification']])



# dict = {"a":[1,2,3,4,5,6],'b':[7,8,9,10,11,12]}
# df = pd.DataFrame(dict)



# #add some rows at a particular index range
# # Create an initial DataFrame
# data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
# 'Age': [25, 30, 35, 28],
# 'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
# df = pd.DataFrame(data)
# # Display the initial DataFrame
# print("Initial DataFrame:")
# print(df)
# # Create data for the new rows
# new_rows = pd.DataFrame([
# {'Name': 'Eve', 'Age': 24, 'City': 'San Francisco'},
# {'Name': 'Frank', 'Age': 32, 'City': 'Miami'},
# {'Name': 'Grace', 'Age': 29, 'City': 'Seattle'}
# ])
# df = pd.concat([df.iloc[:1],new_rows,df.iloc[1:]]).reset_index(drop=True)
# # Display the DataFrame with the new rows
# print("\nDataFrame after adding new rows:")
# print(df)


            # Read and operate csv file using pandas

# data = {
#     "Name" : ['Alice','Bob','Kunal'],
#     'Age' : [20,21,22]
# }

# df = pd.DataFrame(data)

# csv_file_path = 'Output.csv'

# df.to_csv(csv_file_path, index=True, columns=['Name','Age'])

# print(f'Data has been written to {csv_file_path}')

# data = pd.read_csv("Output.csv",nrows=2, usecols = ['Name',1] )
# print(data)


# s = pd.Series(['a','b','a','c','b','a',np.nan,'c','c','c','c'])

# print("Basic Value Count : ")
# print(s.value_counts())

# print(s.value_counts(sort=False))

# print(s.value_counts(ascending=True))

# print(s.value_counts(dropna = False))



# Sample dataset creation
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
#     'Age': [24, 27, 22, 32, 29],
#     'Department': ['HR', 'IT', null, 'Marketing', 'HR'],
#     'Salary': [50000, 60000, 55000, 65000, 62000]
# }

# Create a DataFrame
# df = pd.DataFrame(data)

# # Display the DataFrame
# print("Original DataFrame:\n", df)

# # Generate descriptive statistics
# description = df.describe()

# # Display the descriptive statistics
# print("\nDescriptive Statistics:\n", description)

# df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)


# import pandas as pd
# import numpy as np

# # Sample dataset with missing values
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
#     'Age': [24, np.nan, 22, np.nan, 29],
#     'Department': ['HR', 'IT', np.nan, 'Marketing', 'HR'],
#     'Salary': [50000, 60000, 55000, np.nan, 62000]
# }

# # Create a DataFrame
# df = pd.DataFrame(data)

# # Display the original DataFrame
# print("Original DataFrame:\n", df)

# # Use dropna() with thresh parameter
# # Keep rows with at least 3 non-null values
# df_thresh = df.dropna(thresh=3)

# # Display the DataFrame after dropping rows with less than 3 non-null values
# print("\nDataFrame after applying dropna() with thresh=3:\n", df_thresh)


# # Provide the path to your CSV file
# csv_file_path = 'customer_data.csv' # Replace with the actual path to your CSV file
# # Use read_csv to read the data from the CSV file into a DataFrame
# df = pd.read_csv(csv_file_path)
# # Calculate Mean
# mean = df['Age'].mean()
# # Calculate Median
# median = df['Age'].median()
# #Calculate Mode
# mode = df['Age'].mode().iloc[0]
# # Calculate standard deviation
# std = df['Age'].std()
# # Calculate Minimum values
# minimum = df['Age'].min()
# # Calculate Maximum values
# maximum = df.Age.max()
# print(f" Mean of Age : {mean}")
# print(f" Median of Age : {median}")
# print(f" Mode of Age : {mode}")
# print(f" Standard deviation of Age : {std:.2f}")
# print(f" Maximum of Age : {maximum}")
# print(f" Minimum of Age : {minimum}")


# data = {
#     'ID': [1, 2, 3, 4, 5, 3, 6, 1],
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Charlie', 'Frank', 'Alice'],
#     'Age': [24, 27, 22, 32, 29, 22, 40, 24],
#     'Department': ['HR', 'IT', 'Finance', 'Marketing', 'HR', 'Finance', 'IT', 'HR'],
#     'Salary': [50000, 60000, 55000, 65000, 62000, 55000, 70000, 50000]
# }

# # Create a DataFrame
# df = pd.DataFrame(data)

# # Display the DataFrame
# print(df)
# print(df['Salary'].nunique())
# print(df['Salary'].unique())
# print(df['Salary'].value_counts())
# print(df.sort_values(by=['Name'],ascending = False).head(6))
# condition = df['Department']=='IT'
# print(condition)
# print(df[condition])

# print(df.nlargest(4,'ID'))


# multiple conditions 
# Age = df['Age'] == 22
# dept = df['Department'] == 'Finance'
# sal = df['Salary'] == 55000

# print(df[Age and  dept and sal].head(2))

# print(df['Salary'].groupby(df['Department']).max())

import matplotlib.pyplot as plt
# data = {
#     'months':['jan','feb','march','april','july'],
#     "sales":[5500,4500,7600,6400,6400]
# }

# df = pd.DataFrame(data)
# df.set_index('months',inplace=True)
# df.plot(kind='line')
# print(df['sales'].value_counts())
# df['sales'].value_counts().plot(kind='bar')
# df['sales'].value_counts().plot(kind='barh')
# plt.savefig('picture.png')
# print(df)

# Sample data
# data = {
# 'Hours Studied': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
# 'Exam Scores': [50, 40, 60, 65, 30, 75, 80, 85, 90, 95]
# }
# # Create a DataFrame
# df = pd.DataFrame(data)
# df.plot(kind='bar')
# plt.savefig('corelation')
# # Calculate the correlation
# corelation = df['Hours Studied'].corr(df['Exam Scores'])
# print(corelation)


# data = {
#     'Hours Studied': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     'Stress Levels': [90, 85, 80, 75, 70, 65, 60, 55, 50, 45]  # Stress levels decrease as hours studied increase
# }

# # Create a DataFrame
# df = pd.DataFrame(data)

# # Calculate the correlation
# correlation = df['Hours Studied'].corr(df['Stress Levels'])

# print("Correlation between Hours Studied and Stress Levels:", correlation)


# import pandas as pd
# import numpy as np

# # Sample data
# data = {
#     'Customer_ID': range(1, 21),
#     'Marital_status': np.random.choice(['Single', 'Married', 'Divorced', 'Widowed'], 20),
#     'Payment_method': np.random.choice(['Credit Card', 'Debit Card', 'PayPal', 'Cash'], 20),
#     'Amount': np.random.randint(10, 500, 20)
# }

# # Create DataFrame
# df = pd.DataFrame(data)


# # Display the DataFrame
# print("Sample DataFrame:")
# print(df)

# # Crosstab between Marital_status and Payment_method
# crosstab_result = pd.crosstab(df['Marital_status'], df['Payment_method'],rownames=['status'],colnames=['Method'])

# # Display the crosstab result
# print("\nCrosstab Result:")
# print(crosstab_result)

# # Crosstab with aggregation
# crosstab_agg = pd.crosstab(df['Marital_status'], df['Payment_method'], values=df['Amount'], aggfunc='sum')
# print("\nCrosstab with aggregation (sum of Amount):")
# print(crosstab_agg)

# # Crosstab with margins
# crosstab_margins = pd.crosstab(df['Marital_status'], df['Payment_method'], margins=True)
# print("\nCrosstab with margins:")
# print(crosstab_margins)

# # Crosstab with custom margins name
# crosstab_custom_margins = pd.crosstab(df['Marital_status'], df['Payment_method'], margins=True, margins_name='Total')
# print("\nCrosstab with custom margins name:")
# print(crosstab_custom_margins)

# # Crosstab normalized by index
# crosstab_normalized_index = pd.crosstab(df['Marital_status'], df['Payment_method'], normalize='index')
# print("\nCrosstab normalized by index:")
# print(crosstab_normalized_index)

# # Crosstab normalized by columns
# crosstab_normalized_columns = pd.crosstab(df['Marital_status'], df['Payment_method'], normalize='columns')
# print("\nCrosstab normalized by columns:")
# print(crosstab_normalized_columns)

# # Crosstab normalized by all
# crosstab_normalized_all = pd.crosstab(df['Marital_status'], df['Payment_method'], normalize='all')
# print("\nCrosstab normalized by all:")
# print(crosstab_normalized_all)


                                                   #pivot table

# import pandas as pd

# # Sample data
# data = {
#     'Date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02',
#              '2024-01-03', '2024-01-03', '2024-01-04', '2024-01-04'],
#     'Category': ['Electronics', 'Electronics', 'Electronics', 'Furniture',
#                  'Furniture', 'Furniture', 'Electronics', 'Furniture'],
#     'Product': ['Laptop', 'Smartphone', 'Laptop', 'Table', 'Chair', 'Table',
#                 'Smartphone', 'Chair'],
#     'Revenue': [1000, 800, 1200, 600, 400, 650, 900, 450],
#     'Quantity': [5, 10, 6, 3, 8, 5, 7, 2]
# }

# # Create DataFrame
# df = pd.DataFrame(data)

# # Create pivot table with all parameters
# pivot_table = pd.pivot_table(
#     df,
#     values=['Revenue', 'Quantity'],
#     index=['Category', 'Product'],
#     columns=['Date'],
#     aggfunc={'Revenue': 'sum', 'Quantity': 'sum'},
#     fill_value=0,
#     margins=True,
#     dropna=True,
#     margins_name='Total',
#     observed=False
# )

# print(pivot_table)

# new_df = np.round(pivot_table,2)





import pandas as pd

# Sample data
data = {
    'Date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02',
             '2024-01-03', '2024-01-03', '2024-01-04', '2024-01-04'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Furniture',
                 'Furniture', 'Furniture', 'Electronics', 'Furniture'],
    'Product': ['Laptop', 'Smartphone', 'Laptop', 'Table', 'Chair', 'Table',
                'Smartphone', 'Chair'],
    'Revenue': [1000, 800, 1200, 600, 400, 650, 900, 450],
    'Quantity': [5, 10, 6, 3, 8, 5, 7, 2]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create CSV file
csv_filename = 'sales_data.csv'
df.to_csv(csv_filename, index=False)

print(f"CSV file '{csv_filename}' created successfully.")

# Read the CSV file into a DataFrame
df_from_csv = pd.read_csv(csv_filename)

print("Data read from CSV file:\n", df_from_csv)

# Perform the same operations

# 1. Select rows where the 'Category' is 'Electronics'
electronics_df = df_from_csv.query('Category == "Electronics"')
print("Electronics Category:\n", electronics_df, "\n")

# 2. Select rows where 'Revenue' is greater than 800
high_revenue_df = df_from_csv.query('Revenue > 800')
print("Revenue > 800:\n", high_revenue_df, "\n")

# 3. Select rows where 'Quantity' is between 5 and 10 (inclusive)
quantity_range_df = df_from_csv.query('5 <= Quantity <= 10')
print("Quantity between 5 and 10:\n", quantity_range_df, "\n")

# 4. Select rows where 'Category' is 'Furniture' and 'Revenue' is greater than 500
furniture_high_revenue_df = df_from_csv.query('Category == "Furniture" and Revenue > 500')
print("Furniture Category with Revenue > 500:\n", furniture_high_revenue_df, "\n")

# 5. Select rows where 'Product' is either 'Laptop' or 'Chair'
specific_products_df = df_from_csv.query('Product in ["Laptop", "Chair"]')
print("Products: Laptop or Chair:\n", specific_products_df, "\n")
