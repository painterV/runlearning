import sqlite3

import pandas as pd


# 连接到数据库
conn = sqlite3.connect('comments.db')

# 读取数据库表并将其转换为DataFrame对象
query = 'SELECT * FROM comments where mid = 66391032'
df = pd.read_sql(query, conn)

print(df.head())

print(df.describe())