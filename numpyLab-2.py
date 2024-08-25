import numpy as np


# question - 1
# def identify_extreme_days(temperatures):
#     hot_days = np.where(temperatures > 35)[0]
#     cold_days = np.where(temperatures < 35)[0]
#     return hot_days, cold_days

# temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])
# hot_days, cold_days = identify_extreme_days(temperatures)
# print("Hot days : ")
# print("Day  Temperature")
# for x in hot_days:
#     print(x+1 , "   ",temperatures[x])

# print("Cold days : ")
# print("Day  Temperature")
# for x in cold_days:
#     print(x+1 , "   ",temperatures[x])



# Question - 2
# def split_to_quarters(monthly_sales):
#     return np.split(monthly_sales, 4)

# monthly_sales = np.array([120, 135, 148, 165, 180, 155, 168, 190, 205, 198, 210, 225])
# quarterly_sales = split_to_quarters(monthly_sales)
# for i in range(len(quarterly_sales)):
#     print("Quarter ",i+1," Sales : ")
#     print(quarterly_sales[i])



# question - 3
# def split_customers_by_purchase(customer_ids, last_purchase_days_ago):
#     recent_customers = customer_ids[last_purchase_days_ago <= 30]
#     non_recent_customers = customer_ids[last_purchase_days_ago > 30]
#     return recent_customers, non_recent_customers

# customer_ids = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110])
# last_purchase_days_ago = np.array([5, 15, 20, 25, 30, 35, 40, 45, 50, 55])
# recent_customers, non_recent_customers = split_customers_by_purchase(customer_ids, last_purchase_days_ago)
# print("Active customers (Last purchase <= 30 days ago) : ","\n", recent_customers)
# print("Inactive customers (Last purchase <= 30 days ago) : ","\n", non_recent_customers)


# question - 4

# def combine_employee_data(full_time, part_time):
#     return np.concatenate((full_time, part_time), axis=0)

# full_time_employees = np.array([
#     [101, 'John Doe', 'Full-Time', 55000],
#     [102, 'Jane Smith', 'Full-Time', 60000],
#     [103, 'Mike Johnson', 'Full-Time', 52000]
# ])

# part_time_employees = np.array([
#     [201, 'Alice Brown', 'Part-Time', 25000],
#     [202, 'Bob Wilson', 'Part-Time', 28000],
#     [203, 'Emily Davis', 'Part-Time', 22000]
# ])

# all_employees = combine_employee_data(full_time_employees, part_time_employees)
# print("All Employees:\n", all_employees)


  
                                                 # Assignment

# 1. How to find the mean of every Numpy array in the given list?

# list = [
# np.array([3, 2, 8, 9]),
# np.array([4, 12, 34, 25, 78]),
# np.array([23, 12, 67])
# ]
# ans = []
# for l in list:
#     mean = np.mean(l)
#     ans.append(mean)
   
# print("Mean of each Array : ")
# print(ans)

# -------------------------------------------------------------------------------------------------
# 2. Median of odd Numbers only

# x_odd = np.array([1,2,3,4,5,6,7])
# odd = x_odd[x_odd%3==0]

# median = np.median(odd)
# print(odd)
# print("Printing the Original array: ")
# print(x_odd)
# print("Median of the array that contains odd no of elements: ")
# print(median)

# -------------------------------------------------------------------------------------------------
# 3. Compute std deviation of the Numpy array

# arr = np.array([20,7,2,1,34], dtype=float)

# std = np.std(arr)
# std32 = np.std(arr, dtype=np.float32)
# std64 = np.std(arr, dtype=np.float64)
# print(f"Arr: {arr}")
# print(f"std of arr: {std}")
# print("More precision with float32")
# print(f"std of arr: {std32}")
# print("More accuracy with float64")
# print(f"std of arr: {std64}")

# -------------------------------------------------------------------------------------------------
# 4. Read the data from the CSV file into a Numpy array, Calculate Average of house prices and identify house above the average also save the list of high prices to a new csv file.

# House prices and identify house above average

# house_prices = np.genfromtxt('house_prices.csv', delimiter=',', skip_header=1, usecols=0)


# average_price = np.mean(house_prices)
# print(f"Average House Price: {average_price}")

# high_prices = house_prices[house_prices > average_price]
# print(high_prices)
# np.savetxt('high_house_prices.csv', high_prices, delimiter=',', header='price',fmt='%.2f')




