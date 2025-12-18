from sys import stdin,stdout
from collections import Counter
nmbr=lambda:int(stdin.readline())
lst = lambda: list(map(int,stdin.readline().split()))
for _ in range(1):#nmbr()):
    n=nmbr()
    a=lst()
    b=sorted(a)
    op=0
    for i in range(n):
        if a[i]==b[i]:continue
        op+=1
    if op==0 or op==2:print('YES')
    else:print('NO')