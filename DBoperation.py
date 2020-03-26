# -*- coding: utf-8 -*-

import sqlite3
import pandas as pd

# pandasでカレントディレクトリにあるcsvファイルを読み込む
# csvには、1列目にyear, 2列目にmonth, 3列目にdayが入っているとする。
df = pd.read_csv("table.csv")

# カラム名（列ラベル）を作成。csv file内にcolumn名がある場合は、下記は不要
# pandasが自動で1行目をカラム名として認識してくれる。
df.columns = ['year', 'month', 'day']

dbname = 'db.sqlite3'

conn = sqlite3.connect(dbname)
cur = conn.cursor()

# dbのnameをsampleとし、読み込んだcsvファイルをsqlに書き込む
# if_existsで、もしすでにexpenseが存在していたら、書き換えるように指示
df.to_sql('sample', conn, if_exists='replace')

# 作成したデータベースを1行ずつ見る
select_sql = 'SELECT * FROM sample'
for row in cur.execute(select_sql):
    print(row)

cur.close()
conn.close()