import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = './GPS_2024-01-24_10-57-49_Weather.xlsx'
data = pd.read_excel(file_path)

data['gmt_time'] = pd.to_datetime(data['gmt_time'])


data.set_index('gmt_time', inplace=True)

# Set the style of the visualization
sns.set(style="whitegrid")

# Soil Temperatures at various depths
plt.figure(figsize=(14, 6))
sns.lineplot(data=data[['t_2m:C', 't_0m:C', 't_-5cm:C', 't_-15cm:C', 't_-50cm:C', 't_-150cm:C']], dashes=False, palette='tab10', linewidth=2.5)
plt.title('Soil Temperature at Various Heights and Depths Over Time')
plt.ylabel('Temperature (°C)')
plt.legend(labels=['Temp at 2m', 'Temp at 0m', 'Temp at -5cm', 'Temp at -15cm', 'Temp at -50cm', 'Temp at -150cm'])
plt.show()

# Soil moisture index at various depths
plt.figure(figsize=(14, 6))
sns.lineplot(data=data[['soil_moisture_index_-5cm:idx', 'soil_moisture_index_-15cm:idx', 'soil_moisture_index_-50cm:idx', 'soil_moisture_index_-150cm:idx']], dashes=False, palette='tab10', linewidth=2.5)
plt.title('Soil Moisture Index at Various Depths Over Time')
plt.ylabel('Soil Moisture Index')
plt.legend(labels=['index at -5cm', 'index at -15cm', 'index at -50cm', 'index at -150cm'])
plt.show()

# Volumetric Soil water at various depths
plt.figure(figsize=(14, 6))
sns.lineplot(data=data[['volumetric_soil_water_-5cm:m3m3', 'volumetric_soil_water_-15cm:m3m3', 'volumetric_soil_water_-50cm:m3m3', 'volumetric_soil_water_-150cm:m3m3']], dashes=False, palette='tab10', linewidth=2.5)
plt.title('Volumetric Soil Water at Various Depths Over Time')
plt.ylabel('Volumetric Soil Water Content (m³/m³)')
plt.legend(labels=['index at -5cm', 'index at -15cm', 'index at -50cm', 'index at -150cm'])
plt.show()

# Precipitation over time
plt.figure(figsize=(14, 6))
sns.lineplot(data=data['precip_24h:mm'], color='blue', linewidth=2)
plt.title('Precipitation in 24h Over Time')
plt.ylabel('Precipitation (mm)')
plt.show()

# Wind Speed over time
plt.figure(figsize=(14, 6))
sns.lineplot(data=data['wind_speed_2m:ms'], color='green', linewidth=2)
plt.title('Wind Speed at 2m Over Time')
plt.ylabel('Wind Speed (m/s)')
plt.show()

# Effective Cloud Cover over time
plt.figure(figsize=(14, 6))
sns.lineplot(data=data['effective_cloud_cover:octas'], color='purple', linewidth=2)
plt.title('Effective Cloud Cover Over Time')
plt.ylabel('Cloud Cover (octas)')
plt.show()

# Elevation over time
plt.figure(figsize=(14, 6))
sns.lineplot(data=data['elevation:m'], color='red', linewidth=2)
plt.title('Elevation Over Time')
plt.ylabel('Elevation (m)')
plt.show()
