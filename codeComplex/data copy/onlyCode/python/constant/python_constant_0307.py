k,n,s,p=map(int,input().split(' '))
if (1*n)%s==0:
    need=(1*n)//s
    if need==0 and k%p==0:
        print(k//p)
    elif (k*need)%p==0:
        print((k*need)//p)
    else:
        print(((k*need)//p)+1)    
else:
    need=((1*n)//s)+1
    if need==0 and k%p==0:
        print(k//p)
    elif (k*need)%p==0:
        print((k*need)//p)
    else:
        print(((k*need)//p)+1)    