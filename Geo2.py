import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_excel("./GPS_2024-01-24_10-57-49_Weather.xlsx")

#  plot: Mileage vs Maximum Temperature
plt.figure(figsize=(10, 6))
temperature_plot = sns.pointplot(data=data, x='mileage', y='t_max_2m_24h:C', color='red')
temperature_plot.set_title('Mileage vs Maximum Temperature at 2 m in 24h')
temperature_plot.set_xlabel('Mileage (km)')
temperature_plot.set_ylabel('Maximum Temperature (°C)')
plt.grid(True)
plt.show()
# This graph visualizes the relationship between mileage and maximum temperature observed in 24h at 2m.
# It helps in understanding how temperature varies with distance, potentially indicating climate
# variations along the route.

#  plot: Mileage vs Maximum Temperature
plt.figure(figsize=(10, 6))
temperature_plot = sns.pointplot(data=data, x='mileage', y='t_max_2m_6h:C', color='red')
temperature_plot.set_title('Mileage vs Maximum Temperature at 2 m in 6h')
temperature_plot.set_xlabel('Mileage (km)')
temperature_plot.set_ylabel('Maximum Temperature (°C)')
plt.grid(True)
plt.show()
# This graph visualizes the relationship between mileage and maximum temperature observed in 6h at 2m.
# It helps in understanding how temperature varies with distance, potentially indicating climate
# variations along the route.

#  plot: Mileage vs Wind Speed
plt.figure(figsize=(10, 6))
wind_speed_plot = sns.lineplot(data=data, x='mileage', y='wind_speed_2m:ms', color='blue')
wind_speed_plot.set_title('Mileage vs Wind Speed')
wind_speed_plot.set_xlabel('Mileage (km)')
wind_speed_plot.set_ylabel('Wind Speed (kph)')
plt.grid(True)
plt.show()
# This plot shows how wind speed varies with mileage. Higher wind speeds might be observed in open or elevated areas,
# and this visualization could help identify such trends spatially along the traveled path.

#  plot: Mileage vs Precipitation
plt.figure(figsize=(10, 6))
precipitation_plot = sns.lineplot(data=data, x='mileage', y='precip_24h:mm', color='green')
precipitation_plot.set_title('Mileage vs Precipitation in 24h')
precipitation_plot.set_xlabel('Mileage (km)')
precipitation_plot.set_ylabel('Precipitation (mm)')
plt.grid(True)
plt.show()
# This graph illustrates the precipitation levels in 24h as a function of mileage. It could be useful for identifying
# geographic areas more prone to rain or snow, especially in planning for weather-dependent activities or logistics.

#  plot: Mileage vs Precipitation
plt.figure(figsize=(10, 6))
precipitation_plot = sns.pointplot(data=data, x='mileage', y='precip_1h:mm', color='green')
precipitation_plot.set_title('Mileage vs Precipitation in 1h')
precipitation_plot.set_xlabel('Mileage (km)')
precipitation_plot.set_ylabel('Precipitation (mm)')
plt.grid(True)
plt.show()
# This graph illustrates the precipitation levels in 1h as a function of mileage. It could be useful for identifying
# geographic areas more prone to rain or snow, especially in planning for weather-dependent activities or logistics.

#  plot: Mileage vs Precipitation
plt.figure(figsize=(10, 6))
precipitation_plot = sns.pointplot(data=data, x='mileage', y='precip_5min:mm', color='green')
precipitation_plot.set_title('Mileage vs Precipitation in 5min')
precipitation_plot.set_xlabel('Mileage (km)')
precipitation_plot.set_ylabel('Precipitation (mm)')
plt.grid(True)
plt.show()
# This graph illustrates the precipitation levels in 5min as a function of mileage. It could be useful for identifying
# geographic areas more prone to rain or snow, especially in planning for weather-dependent activities or logistics.

# Mileage vs Effective Cloud Cover
plt.figure(figsize=(10, 6))
cloud_cover_plot = sns.pointplot(data=data, x='mileage', y='effective_cloud_cover_mean_24h:octas', color='gray')
cloud_cover_plot.set_title('Mileage vs Effective Cloud Cover mean in 24h')
cloud_cover_plot.set_xlabel('Mileage (km)')
cloud_cover_plot.set_ylabel('Cloud Cover (octas)')
plt.grid(True)
plt.show()
# This plot shows the effective cloud cover over the route, measured in octas, which can help in understanding
# weather conditions related to cloudiness at different points along the path.

# Mileage vs Effective Cloud Cover
plt.figure(figsize=(10, 6))
cloud_cover_plot = sns.pointplot(data=data, x='mileage', y='effective_cloud_cover_mean_6h:octas', color='gray')
cloud_cover_plot.set_title('Mileage vs Effective Cloud Cover mean in 6h')
cloud_cover_plot.set_xlabel('Mileage (km)')
cloud_cover_plot.set_ylabel('Cloud Cover (octas)')
plt.grid(True)
plt.show()


# Mileage vs Effective Cloud Cover
plt.figure(figsize=(10, 6))
cloud_cover_plot = sns.pointplot(data=data, x='mileage', y='effective_cloud_cover_mean_12h:octas', color='gray')
cloud_cover_plot.set_title('Mileage vs Effective Cloud Cover mean in 12h')
cloud_cover_plot.set_xlabel('Mileage (km)')
cloud_cover_plot.set_ylabel('Cloud Cover (octas)')
plt.grid(True)
plt.show()


# Mileage vs Elevation
plt.figure(figsize=(10, 6))
elevation_plot = sns.pointplot(data=data, x='mileage', y='elevation:m', color='purple')
elevation_plot.set_title('Mileage vs Elevation')
elevation_plot.set_xlabel('Mileage (km)')
elevation_plot.set_ylabel('Elevation (m)')
plt.grid(True)
plt.show()
# This line plot visualizes how the elevation changes with mileage, useful in understanding the terrain,
# and how elevation influences weather and transportation conditions.

# Mileage vs Clear Sky Radiation
plt.figure(figsize=(10, 6))
radiation_plot = sns.lineplot(data=data, x='mileage', y='clear_sky_rad:W', color='orange')
radiation_plot.set_title('Mileage vs Clear Sky Radiation')
radiation_plot.set_xlabel('Mileage (km)')
radiation_plot.set_ylabel('Clear Sky Radiation (W)')
plt.grid(True)
plt.show()
# This graph represents the variation in clear sky radiation, measured in watts, along the route, indicating
# potential solar exposure and its impact on conditions along the path.
