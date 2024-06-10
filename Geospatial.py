import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_excel("/CITM/Aposys/GPS_2024-01-24_10-57-49_Weather.xlsx")

# Filter the necessary columns
plot_data = data[['latitude', 'longitude', 't_-15cm:C']]

# Set up the seaborn plot
plt.figure(figsize=(10, 6))
scatter_plot = sns.scatterplot(data=plot_data, x='longitude', y='latitude', hue='t_-15cm:C', 
                               palette='viridis', s=100)

#  plot 
scatter_plot.set_title('Spatial Distribution of Soil Temperature at 15 cm Depth')
scatter_plot.set_xlabel('Longitude')
scatter_plot.set_ylabel('Latitude')
plt.legend(title='Soil Temp at 15 cm (°C)', loc='best')
plt.grid(True)

plt.show()

