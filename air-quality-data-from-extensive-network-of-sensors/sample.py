import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
sensors_df = pd.read_csv("sensor_locations.csv")


december_df = pd.read_csv("december-2017.csv")
print(december_df.columns.values)

df_140 = december_df[['UTC time', '140_temperature', '140_humidity', '140_pressure', '140_pm1', '140_pm10', '140_pm25']]
print(df_140.head())

# sns.lmplot(x='UTC time', y='140_humidity', data=df_140)