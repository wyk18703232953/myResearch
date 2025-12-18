from math import ceil

n=int(input())
d={1:[1],2:[1,2],3:[1,1,3]}
if n in d:
    for i in d[n]:
        print(i,end=' ')
    exit()
def f(n):
    if n in d:
        return d[n]
    odds=ceil(n/2)
    lis=[1]*odds
    even=n//2
    lis1=f(even)
    for i in range(len(lis1)):
        lis1[i]*=2
    return lis+lis1
ans=f(n)
for i in ans:
    print(i,end=' ')