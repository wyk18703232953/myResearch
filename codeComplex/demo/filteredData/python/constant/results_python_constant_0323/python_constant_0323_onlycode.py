a=list(map(int, input().split()))
h=0
for i in range(14):
    b=a[:]
    if i==13:
        j=0
    else:
        j=i+1
    if a[i]>0:
        c=0
        t=b[i]%14
        x=b[i]//14
        b[i]=0
        # print(b)
        for i in range(14):
            b[i]+=x
        # print(b)
        while t>0:
            b[j]+=1
            j+=1
            if j==14:
                j=0
            t-=1
        for i in range(14):
            if b[i]%2==0:
                c+=b[i]
        # print(b)
        if c>h:
            h=c
print(h)






