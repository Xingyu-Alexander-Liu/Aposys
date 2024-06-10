import pandas as pd

# Load the dataset
file_path = '/CITM/Aposys/GPS_2024-01-24_10-57-49_Weather.xlsx'
data = pd.read_excel(file_path)

# Display the first few rows of the dataset
data.head()

