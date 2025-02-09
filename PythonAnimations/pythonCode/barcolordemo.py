import matplotlib.pyplot as plt

# Create data for the bar chart
categories = ['A', 'B', 'C']
values = [15, 10, 12]

# Define custom colors for the bars
colors = ['red', 'green', 'blue']

# Create the bar chart
plt.bar(categories, values, color=colors)

# Customize the legend entries
legend_labels = ['Category A', 'Category B', 'Category C']
plt.legend(legend_labels)

# Display the chart
plt.show()