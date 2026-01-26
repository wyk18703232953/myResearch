import math
n=int(input())
lst = list(map(int, input().strip().split(' ')))
#n,r = map(int, input().strip().split(' '))
p=max(lst)
ind=lst.index(p)
if p==1:
    lst[ind]=2
else:
    lst[ind]=1
lst.sort()
for j in range(n):
    print(lst[j],end=" ")