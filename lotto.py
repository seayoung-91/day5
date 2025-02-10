import random

def lotto_f():
    lotto=[]
    for i in range(0,6):
        while True:
            temp=random.randint(1,45)
            if temp not in lotto:
                lotto.append(temp)
                break
    return lotto

# werwerwerwer
# check 555123234324aaaaa
# weeeee



if __name__ == '__main__':
    lotto=lotto_f()
#%%%%%%%%%%%%%%
    #234234234324324234234234324234