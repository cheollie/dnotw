import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load your IMF data into a pandas DataFrame (assuming it's in CSV format)
data = pd.read_csv('imf_data.csv')

# Convert the time column to datetime format
data['Time'] = (data['Hour']+data['Day']*24)/(24*30)#pd.to_datetime(data[['Year', 'Day', 'Hour']], format='%Y %j %H')

# Calculate basic statistics for each IMF component
mean_Bt = data['WIND Bt'].mean()
std_Bt = data['WIND Bt'].std()

mean_Bx = data['WIND Bx_gse'].mean()
std_Bx = data['WIND Bx_gse'].std()

mean_By = data['WIND By_gse'].mean()
std_By = data['WIND By_gse'].std()

mean_Bz = data['WIND Bz_gse'].mean()
std_Bz = data['WIND Bz_gse'].std()

# Define threshold criteria for event detection (customize these based on your criteria)
threshold_Bx = 100.0  # Example threshold for Bx component
threshold_By = 100.0   # Example threshold for By component
threshold_Bz = 100.0   # Example threshold for Bz component

# Detect reconnection events based on the criteria
reconnection_events = data[
    (data['WIND Bx_gse'] > threshold_Bx) &
    (data['WIND By_gse'] < -threshold_By) &
    (data['WIND Bz_gse'].abs() > threshold_Bz)
]

# Calculate the frequency of reconnection events per unit time
event_frequency = len(reconnection_events) / (data['Time'].max() - data['Time'].min())#.total_seconds()

# Print basic statistics and event frequency
print(f"Mean Bt: {mean_Bt}, Std Bt: {std_Bt}")
print(f"Mean Bx: {mean_Bx}, Std Bx: {std_Bx}")
print(f"Mean By: {mean_By}, Std By: {std_By}")
print(f"Mean Bz: {mean_Bz}, Std Bz: {std_Bz}")
print(f"Reconnection Event Frequency: {event_frequency} events per second")

# Visualize the IMF data and reconnection events
plt.figure(figsize=(12, 6))
#plt.plot(data['Time'], data['WIND Bx_gse'], label='Bx')
#plt.plot(data['Time'], data['WIND By_gse'], label='By')
#plt.plot(data['Time'], data['WIND Bz_gse'], label='Bz')
plt.plot(data['Time'], pow(data['WIND Bx_gse']**2+data['WIND By_gse']**2+data['WIND Bz_gse']**2,0.5), label='magnitude')
plt.plot(data['Time'], data['WIND Bz_gse'], label='Bz')
plt.scatter(reconnection_events['Time'], reconnection_events['WIND Bx_gse'], c='red', label='Reconnection Events')
plt.xlabel('Month')
plt.ylabel('IMF Component (nT)')
plt.legend()
plt.title('IMF and Reconnection Events (2020-2023)')
plt.grid(True)
plt.show()
