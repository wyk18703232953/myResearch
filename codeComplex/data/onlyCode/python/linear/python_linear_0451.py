n,m=map(int,input().split())
s=input()
t=input()
if n-1>m:
    print('NO')
else:
    try:
        a=s.index('*')
    except:
        a=-1
    if a==-1:
        if s==t:
            print('YES')
        else:
            print('NO')
    else:
        f=True
        for i in range(a):
            if s[i]!=t[i]:
                print('NO')
                exit()
        i=1
        while m-i>=a and n-i>a:
            if s[n-i]!=t[m-i]:
                print('NO')
                exit()
            i+=1
        print('YES')