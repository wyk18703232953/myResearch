import sys
import bisect
#input=sys.stdin.readline
l=input().split()
a=l[0]
b=l[1]
p=[]
for i in range(len(a)):
    for j in range(len(b)):
        ok=a[:i+1]+b[:j+1]
        p.append(ok)
print(min(p))
