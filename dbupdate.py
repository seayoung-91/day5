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
selname=input("수정할 상품명 선택:")
selwhat=int(input("1.판매가 2.구매가 3.둘모두:"))
if selwhat==1:
    sale=input("판매가 입력:")
    sqlUpdate="update 상품 set 판매가="+sale+" where 상품명='"+selname+"';"
elif selwhat==2:
    buy = input("구매가 입력:")
    sqlUpdate = "update 상품 set 구매가=" + buy + " where 상품명='" + selname + "';"
elif selwhat==3:
    sale = input("판매가 입력:")
    buy = input("구매가 입력:")
    sqlUpdate = "update 상품 set 판매가="+sale+", 구매가=" + buy
    sqlUpdate += " where 상품명='" + selname + "';"
cur.execute(sqlUpdate)

cur.execute(sqlSelectAll)
res=cur.fetchall()
pdresult=pd.DataFrame(res)
print(pdresult)

conn.commit()
conn.close()