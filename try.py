while True:
    i=int(input("enter:"))
    j=int(input("enter:"))
    try:
        res=i/j
        print(res)
    except ZeroDivisionError as e:
        print(e)
        print("j는 0으로 하면 안된다.")
