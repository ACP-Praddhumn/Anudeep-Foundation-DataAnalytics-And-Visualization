import numpy as np
import matplotlib.pyplot as plt

# question - 1 :  Analyze the Relationship Between House Size and Selling Prices

# Input data
square_footage = np.array([1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000])
selling_prices = np.array([250, 290, 315, 380, 410, 450, 500, 525, 570, 610])

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(square_footage, selling_prices, color='blue')
plt.title('Relationship Between House Size and Selling Prices')
plt.xlabel('Square Footage')
plt.ylabel('Selling Price (in thousands)')
plt.grid(True)
plt.show()


# question - 2: Create a Pie Chart to Visualize Monthly Income by Source

# Input data
income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other']
monthly_income = [5000, 1500, 1000, 600, 400]

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(monthly_income, labels=income_sources, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Monthly Income by Source')
plt.show()


# question - 3:  Create a Pie Chart to Illustrate Revenue Distribution Across Business Segments

# Input data
segments = ['Product A', 'Product B', 'Services', 'Licensing']
revenue_percentages = [45, 25, 15, 15]

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(revenue_percentages, labels=segments, autopct='%1.1f%%', startangle=140)
plt.title('Revenue Distribution Across Business Segments')
plt.show()


# question - 4: Subplots Comparing Sales Performance of Different Product Categories

# Input data
months = np.arange(1, 13)
electronics_sales = np.array([25000, 28000, 31000, 27000, 30000, 32000, 35000, 36000, 38000, 39000, 41000, 42000])
clothing_sales = np.array([15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000])
home_garden_sales = np.array([18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000])
sports_outdoors_sales = np.array([12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000])

# Create subplots
plt.figure(figsize=(14, 10))

plt.subplot(2, 2, 1)
plt.plot(months, electronics_sales, marker='o', color='blue')
plt.title('Electronics Sales Over Time')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(months, clothing_sales, marker='o', color='green')
plt.title('Clothing Sales Over Time')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.grid(True)

plt.subplot(2, 2, 3)
plt.plot(months, home_garden_sales, marker='o', color='orange')
plt.title('Home & Garden Sales Over Time')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.grid(True)

plt.subplot(2, 2, 4)
plt.plot(months, sports_outdoors_sales, marker='o', color='red')
plt.title('Sports & Outdoors Sales Over Time')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.grid(True)

plt.tight_layout()
plt.show()