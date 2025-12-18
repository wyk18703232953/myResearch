def iscomposite(value):
    for i in range(2,value):
        if(value%i==0):
            return '1'
    else:
        return '0'



n=int(input())
for i in range(4,n):
    a=i
    b=n-i
    if(iscomposite(a)=='1' and iscomposite(b)=='1'):
        print(a,b)
        break
    else:
        continue
