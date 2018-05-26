import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.rc("font", size=14)

from sklearn import preprocessing

sns.set(style='white')  # white beackground for seaborn plots
sns.set(style='whitegrid', color_codes=True)

train_df = pd.read_csv("air-quality-data-from-extensive-network-of-sensors/means_sensor.csv")

print(train_df.head())
