n=int(input())
if n>=0:
    print(n)
else:
    a=str(n)
    a=a[1::]
    if len(a)>2:
        a=a[::-1][1::][::-1]
        num1=int(a)
        a=str(n)
        a=a[1::]
        b=a[::-1]
        p1=b[0]
        p2=b[2::]
        p=p1+p2
        p=p[::-1]
        num2=int(p)
        small=min(num1,num2)
        print(-1*small)
        
    elif len(a)==2:
        m=a[0]
        n=a[1]
        small=min(int(m),int(n))
        print(-1*small)
    