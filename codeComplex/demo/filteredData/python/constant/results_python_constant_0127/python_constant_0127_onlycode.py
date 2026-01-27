money=input()
initi=money
# if money>0:pass
    
if int(money)<0:
    lst_dig=money[-1]
    lsec_dig=money[-2]
    if int(lst_dig)>int(lsec_dig):money=money[:-2]+money[-2]
    else:money=money[:-2]+money[-1]
    print(int(money))
else:
    lst_dig=money[-1]
    lsec_dig=money[-2]
    if int(lst_dig)>int(lsec_dig):money=money[:-2]+money[-1]
    else:money=money[:-2]+money[-2]
    if int(initi)>=int(money):
        print(initi)
    else:
        print(money)
    