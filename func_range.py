# func_range.py 변수의 범위. 기억클래스
# a=1
# def vartest(b):
#     b = b + 1 #지역변수 = 영역내에서만 사용가능
#     return b
# a=vartest(a)
# print(a)

def add(a,b):
    return a+b

result = add(3,4)
print(result)

add = lambda a, b: a+b
result = add(3, 4)
print(result)

