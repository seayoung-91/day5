import pymysql #패키지 설치.
import pandas as pd

conn = pymysql.connect(host='localhost',user='root', password='1234', db="상품판매db", charset='utf8')#1. connection(연결)
cur=conn.cursor()
sqlSelectAll ='select * from 상품;'
cur.execute(sqlSelectAll)
res=cur.fetchall()
pdresult=pd.DataFrame(res)
print(pdresult)

print("="*30)
selname=input("삭제할 상품명 선택:")
sqlDelete="delete from 상품 where 상품명='"+selname+"';"
cur.execute(sqlDelete)

cur.execute(sqlSelectAll)
res=cur.fetchall()
pdresult=pd.DataFrame(res)
print(pdresult)

conn.commit()
conn.close()