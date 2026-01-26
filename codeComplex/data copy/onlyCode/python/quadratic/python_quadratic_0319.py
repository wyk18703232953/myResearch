n,m=map(int,input().split())
lst=list(map(int,input().split()))
maxx=0
arr=[0]*(n+1)
for i in range(n):
    summ=0
    for j in range(i,n):
        summ+=lst[j]
        arr[j-i]=max(arr[j-i], summ/(j-i+1))
print(max(arr[m-1:]))