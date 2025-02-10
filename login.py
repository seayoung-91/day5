import pymysql #패키지 설치.
import pandas as pd

while True:
    conn = pymysql.connect(host='localhost',user='root',
                           password='1234',db="상품판매db", charset='utf8')
    cur=conn.cursor()
    userid=input("id:")
    userpass=input("pass:")
    sql ="select id, pass, 구분 from 고객 where id='"+userid+"';"
    cur.execute(sql)
    resultSearch = cur.fetchone()
    if resultSearch is None:
        print("id가 잘못됨. 다시 로그인 해!!!")
        continue
    if resultSearch[1]==userpass:
        print(f"{resultSearch[0]}님 환영합니다.")
        break

conn.commit()
conn.close()
