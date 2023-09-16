import pandas as pd

#读取数据
nba_df = pd.read_csv('./all_seasons.csv')

print(nba_df.info())

#去除缺失值
nba_df.dropna(inplace=True)

#去除重复值
nba_df.drop_duplicates(inplace=True)

#获取年龄的统计值
nba_df.describe()['']