
import matplotlib.pyplot as plt
sizes = [40,35,25]
labels = ["Java","Python","C"]

plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Pie Chart")
plt.show()