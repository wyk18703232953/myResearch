n=int(input())
a=list(map(int, input().rstrip().split()))
a.sort()
sum1=0
rem=sum(a)
i=len(a)-1
c=0
while(sum1<=rem):
    sum1+=a[i]
    rem=sum(a)-sum1
    i-=1
    c+=1
print(c)