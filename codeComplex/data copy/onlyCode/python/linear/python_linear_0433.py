# import os

n = int(input())

r = []
for _ in range(n):
    a,b,c,d = map(int,input().split())
    r.append(sum([a,b,c,d]))

thomas = r[0]
print(sorted(r, reverse=True).index(thomas)+1)
