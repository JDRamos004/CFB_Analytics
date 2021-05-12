import pandas as pd
import pymysql

pd.set_option('display.max_rows', None)
# df_cfb = pd.read_csv('CFBAnalytics.csv')
# print(df_cfb)
conn = pymysql.connect(database='cfb_data', user='root',
                       password='')
cursor = conn.cursor()

insert_query = 'INSERT INTO team_wl VALUES '

for i in range(df_cfb.shape[0]):
    insert_query += '('

    for j in range(df_cfb.shape[1]):
        if j == 0 or j == 7:
            insert_query += "'" + \
                str(df_cfb[df_cfb.columns.values[j]][i]) + "'" + ', '
        else:
            insert_query += str(df_cfb[df_cfb.columns.values[j]][i]) + ', '

    insert_query = insert_query[:-2] + '), '

insert_query = insert_query[:-2] + ';'

cursor.execute(insert_query)
conn.commit()
conn.close()
