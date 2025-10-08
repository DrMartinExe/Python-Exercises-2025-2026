# ==========================================
# Week 3 Solutions: Visualizing Data with Matplotlib
# ==========================================
# Save this file as solutions3.py

# Exercise 1: Installing Matplotlib
# Run in terminal:
# pip install matplotlib pandas

# Exercise 2: Importing Libraries
import matplotlib.pyplot as plt
import pandas as pd
print("Matplotlib and pandas loaded successfully!")

# Exercise 3: Line Plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.title("Simple Line Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# Exercise 4: Scatter Plot
x_values = [1, 2, 3, 4, 5]
y_values = [2, 3, 5, 7, 11]
plt.scatter(x_values, y_values)
plt.title("Simple Scatter Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()

# Exercise 5: Customizing Plots
plt.scatter(x_values, y_values, color='green', s=100)
plt.grid(True)
plt.title("Prime Numbers Growth")
plt.xlabel("Position")
plt.ylabel("Prime Value")
plt.show()

# Exercise 6: Using a Colormap
x = list(range(1, 51))
y = [value ** 2 for value in x]
plt.scatter(x, y, c=y, cmap='plasma', s=60)
plt.title("Squares with Colormap")
plt.xlabel("Value")
plt.ylabel("Square")
plt.colorbar(label="Square Value")
plt.show()

# Exercise 7: Bar Chart
categories = ['Apples', 'Bananas', 'Cherries']
values = [10, 15, 7]
plt.bar(categories, values)
plt.title("Fruit Sales")
plt.xlabel("Fruit Type")
plt.ylabel("Quantity Sold")
plt.show()

# Exercise 8: Loading Data with pandas
data = {'Year': [2020, 2021, 2022, 2023], 'Sales': [150, 200, 250, 300]}
df = pd.DataFrame(data)
plt.plot(df['Year'], df['Sales'], marker='o')
plt.title("Sales Over Time")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.show()

# Final Challenge: Combining Skills
x = list(range(1, 21))
y = [val ** 2 for val in x]
plt.scatter(x, y, c=y, cmap='viridis', s=[v/2 for v in y])
plt.title("Square Numbers Visualization")
plt.xlabel("X Value")
plt.ylabel("Square Value")
plt.grid(True)
plt.colorbar(label="Square Value")
plt.savefig("squares_plot.png")
plt.show()
