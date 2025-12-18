import math
n,k=map(int,input().split())
for _ in range(k):
    l,r=map(int,input().split())
for i in range(1,n+1):
    if i%2==0:
        print('0',end='')
    else:
        print('1',end='')
print()

