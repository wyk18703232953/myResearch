from sys import stdin,stdout
from math import ceil
nmbr = lambda: int(stdin.readline())
lst = lambda: list(map(int, stdin.readline().split()))
for _ in range(1):#nmbr()):
    n=nmbr()
    a=lst()
    p=0
    ans=float('inf')
    for i in range(n):
        turns=ceil((a[i]-i)/n)
        if turns<ans:
            ans=turns
            p=i
    print(p+1)