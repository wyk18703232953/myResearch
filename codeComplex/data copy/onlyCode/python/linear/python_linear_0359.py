import sys
from math import sqrt,log2
from collections import Counter

input = lambda: sys.stdin.readline().rstrip("\r\n")

n=input()
ct=0
i=0
s=[]
while i <len(n):
    if not int(n[i])%3:
        ct+=1
        s.clear()
    else:
        t=int(n[i])%3
        if 3-t in s:
            ct+=1
            s.clear()
        else:
            s.append(t)
    if len(s)==3:
        ct+=1
        s.clear()
    i+=1

print(ct)