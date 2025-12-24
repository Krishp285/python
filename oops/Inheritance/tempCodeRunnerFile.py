import matplotlib.pyplot as plt
items = ["A", "B", "C", "D"]
values = [25, 40, 30, 20]

plt.bar(items, values, color='green', edgecolor='black', width=0.6)
plt.title("Styled Bar Chart")
plt.xlabel("Items")
plt.ylabel("Values")

# Displaying values on bars
for i in range(len(values)):
    plt.text(i, values[i]+1, values[i])

plt.show()
