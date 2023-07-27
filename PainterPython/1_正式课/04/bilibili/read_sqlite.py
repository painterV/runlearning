import sqlite3

import pandas as pd


# 连接到数据库
conn = sqlite3.connect('comments.db')

# 读取数据库表并将其转换为DataFrame对象
query = 'SELECT * FROM comments'
df = pd.read_sql(query, conn)

print(df.head())

print(df.describe())

print(df.count())

# 保存到csv文件中
df.to_csv('comments.csv', index=False)