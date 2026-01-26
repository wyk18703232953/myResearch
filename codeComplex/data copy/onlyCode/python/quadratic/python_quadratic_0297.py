n=int(input())
a=list(map(int,input().split()))
p=0
while p+1<len(a) and a[p]==a[p+1]:
    p+=2
c=0
while p<len(a):
    if p+1<len(a):
        i=a.index(a[p],p+1)
        c+=i-p-1
        tmp=a.pop(i)
        a.insert(p,tmp)
    while p+1<len(a) and a[p]==a[p+1]:
        p+=2
print(c)