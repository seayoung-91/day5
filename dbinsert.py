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
pname, salePrice, buyPrice=input("상품명,판매가,구매가 입력").split(',')
sqlInsert="insert into 상품(상품명, 판매가, 구매가) values('"+pname+"',"+salePrice+","+buyPrice+");"
cur.execute(sqlInsert)

cur.execute(sqlSelectAll)
res=cur.fetchall()
pdresult=pd.DataFrame(res)
print(pdresult)

conn.commit()
conn.close()

