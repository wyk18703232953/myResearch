n=int(input())
s=input()
l=[]
total=0
p=0
for i in range(0,450):
    sum1=0
    flag=1
    r=0
    for k in range(n):
        sum1=sum1+int(s[k])
        if(sum1>i):
            flag=0
        if(sum1==i):
            sum1=0
            r=r+1
    if(r>=2 and sum1==0 and flag==1):
        print("YES")
        p=1
        break
if(p==0):
    print("NO")