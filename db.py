import pymysql #패키지 설치.
import pandas as pd

conn = pymysql.connect(host='localhost',user='root', password='1234',
                       db="상품판매db", charset='utf8')#1. connection(연결)
cur=conn.cursor()
sql ='select * from 상품;'
cur.execute(sql)

# while True:
#     row = cur.fetchmany(5)
#     if row is None:
#         break
#     for i in row:
#         print(i)

# while True:
#     row = cur.fetchone()
#     while row is not None:
#         print(row)
#     else:
#         break

res=cur.fetchall()
# for row in res:
#     print(str(row))
res=pd.DataFrame(res)
print(res)

conn.commit()
conn.close()
