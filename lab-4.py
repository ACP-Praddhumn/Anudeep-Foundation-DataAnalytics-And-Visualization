import matplotlib.pyplot as plt

# Visualize the Daily Temperature Changes Over Time in a City
# Input data
days = list(range(1, 32))  # Days of the month
temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78, 80, 81, 82, 83, 82, 80, 78, 76, 74, 71]

# Plotting the data
plt.figure(figsize=(10, 5))
plt.plot(days, temperature, marker='o', linestyle='-', color='blue')
plt.title('Daily Temperature Changes Over Time')
plt.xlabel('Day of the Month')
plt.ylabel('Temperature (°F)')
plt.grid(True)
plt.show()




# Create a Line Plot to Visualize the Daily Closing Prices of a Stock Over a Year
# Input data
days = list(range(1, 78))  # Days of the period
stock_prices = [
    100, 105, 110, 115, 112, 120, 118, 125, 128, 130, 132, 135, 138, 140, 142, 144, 
    145, 148, 150, 155, 160, 158, 162, 165, 170, 172, 175, 178, 180, 182, 185, 188, 
    190, 192, 195, 198, 200, 198, 195, 193, 190, 188, 185, 182, 180, 178, 175, 172, 
    170, 168, 165, 162, 160, 158, 155, 152, 150, 148, 145, 143, 140, 138, 135, 132, 
    130, 128, 125, 123, 120, 118, 115, 112, 110, 108, 105, 103, 100
]

# Plotting the data
plt.figure(figsize=(12, 6))
plt.plot(days, stock_prices, marker='o', linestyle='-', color='green')
plt.title('Daily Closing Prices of a Stock Over a Period')
plt.xlabel('Day')
plt.ylabel('Stock Price ($)')
plt.grid(True)
plt.show()
