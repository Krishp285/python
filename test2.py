import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data for Impact
impact_data = {
    'Category': [
        'Interactive Heritage Learning',
        'Scales Access to Cultural Sites',
        'Govt Digital Preservation Goals',
        'Tourism-Community Collaboration',
        'Engagement Tracking'
    ],
    'Value': [25, 15, 20, 10, 30] # Unequal distribution for Impact
}
impact_df = pd.DataFrame(impact_data)

# Data for Benefits
benefits_data = {
    'Category': [
        'Cultural Education',
        'Tourism Growth',
        'Reduced Site Degradation',
        'Local Artist Involvement',
        'Global Awareness',
        'Funding for Heritage Tech'
    ],
    'Value': [30, 20, 10, 25, 15, 20] # Unequal distribution for Benefits
}
benefits_df = pd.DataFrame(benefits_data)

# Combine all categories and values into a single DataFrame
all_categories = pd.concat([impact_df['Category'], benefits_df['Category']])
all_values = np.concatenate([impact_df['Value'], benefits_df['Value']])

combined_df = pd.DataFrame({'Category': all_categories, 'Value': all_values})

# Create a figure and an axes object
fig, ax = plt.subplots(figsize=(10, 10))

# Plot the pie chart
ax.set_title('Impact & Benefits of AR Heritage Platform', fontsize=16)

# Generate a color map that avoids black
colors = plt.get_cmap('tab20')(np.linspace(0, 1, len(combined_df)))

wedges, texts, autotexts = ax.pie(
    combined_df['Value'],
    labels=combined_df['Category'],
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    radius=0.4, # Setting the radius to a smaller value
    textprops={'fontsize': 10}
)

# Ensure the percentages are visible and don't overlap with labels
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)

ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Save the plot
plt.savefig('combined_pie_chart_unequal.png')

# Show the plot
plt.show()