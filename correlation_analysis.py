import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = '/CITM/Aposys/GPS_2024-01-24_10-57-49_Weather.xlsx'
data = pd.read_excel(file_path)


print(data.dtypes)

# Exclude non-numerical columns
columns_to_exclude = ['filenames', 'gmt_time', 'toronto_time', 'test_start', 'coordinates', 'validdate','subdivision','milepost','weather_time']
numerical_data = data.drop(columns=columns_to_exclude, errors='ignore')

# Compute the correlation matrix for numerical columns
correlation_matrix = numerical_data.corr()

# Set up the matplotlib figure
plt.figure(figsize=(15, 10))

# Generate a heatmap
sns.heatmap(correlation_matrix, annot=False, cmap='coolwarm', fmt=".1f", linewidths=.5)
plt.title('Correlation Matrix of Numerical Variables')
plt.show()