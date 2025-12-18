# import os

n,m = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

r = []

for i in a:
    if i in b:
        r.append(i)
print(' '.join(map(str, r)))


