import pandas as pd

sensors_df = pd.read_csv("sensor_locations.csv")
print(sensors_df.head())
print(sensors_df.shape)
print(sensors_df.tail())

december_df = pd.read_csv("december-2017.csv")
