import matplotlib.pyplot as plt
# line plot
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.plot(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Plot")
plt.show()

# bar plot
categories = ["A", "B", "C", "D", "E"]
values = [10, 15, 7, 12, 20]
plt.bar(categories, values)
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Plot")
plt.show()

# scatter plot
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.scatter(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter Plot")
plt.show()

# histogram
import matplotlib.pyplot as plt
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
plt.hist(data, bins=10, edgecolor='black')
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()
