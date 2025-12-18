from collections import defaultdict as dd
d=dd(int)
n,m=map(int,input().split())
arr=list(map(int,input().split()))
has=False
count=0
d[0] =1
total=0
for i in range(n):
    if arr[i] >m:
        count  +=1
    if arr[i] <m:
        count -=1
    if arr[i] ==m:
        has=True
    if has:
        total +=d[count] +d[count-1]
    else:
        d[count] +=1
print(total)