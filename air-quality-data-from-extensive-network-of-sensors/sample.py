# import pandas as pd
# import seaborn as sns
# from matplotlib import pyplot as plt
# sensors_df = pd.read_csv("sensor_locations.csv")
#
#
# december_df = pd.read_csv("december-2017.csv")
# print(december_df.columns.values)
#
# df_140 = december_df[['UTC time', '140_temperature', '140_humidity', '140_pressure', '140_pm1', '140_pm10', '140_pm25']]
# print(df_140.head())
#
# # sns.lmplot(x='UTC time', y='140_humidity', data=df_140)

a = (
    'MULTIPOLYGON(((17.0292687721708 52.4081601723822,17.0256097251908 52.4083768336072,17.0259655163574 52.4106114420041,17.0296247457067 52.4103947682457,17.0292687721708 52.4081601723822)))',)


def parser_krzys(a):
    l = []
    for pair in a[0].split('(((')[1].split(')))')[0].split(','):
        a = float(pair.split(' ')[0])
        b = float(pair.split(' ')[1])
        l.append((a, b))
    return l


print(parser_krzys(a))
