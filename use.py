# import sys
# print(sys.path)
# sys.path.append(r"D:\startPy\day5\sub")
# print(sys.path)
from sub.calc import *

data1=int(input("숫자넣어"))
data2=int(input("숫자넣어"))
addres=add(data1,data2)
print("{0}+{1}={2}".format(data1,data2,addres))
print("%d-%d=%d"%(data1,data2,sub(data1,data2)))
print(f"{data1}*{data2}={mul(data1,data2)}")
