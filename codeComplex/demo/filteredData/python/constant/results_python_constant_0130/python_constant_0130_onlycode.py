a=int(input())
if a>0:
    print(a)
else:
    a=a-2*a
    k=a//10
    b=a%10
    c=(a//100)*10+b
    if k<c:
        if k!=0:
            print('-%d' %k)
        else:
            print(k)
    else:
        if c!=0:
            print('-%d' %c)
        else:
            print(c)