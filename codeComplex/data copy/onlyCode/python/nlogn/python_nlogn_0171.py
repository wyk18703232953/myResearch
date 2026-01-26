# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 19:45:38 2019

@author: avina
"""

n = int(input())

l = []
for _ in range(n):
    k,m = map(int, input().strip().split())
    l.append((k,m))

l.sort(key=lambda x:x[0]+x[1])

last = 0
ans = 1

for i in range(1,n):
   if l[i][0] - l[i][1] >= l[last][0] - l[last][1] and abs(l[i][0] - l[last][0]) >= l[i][1] + l[last][1] :
       last = i
       ans = ans + 1
       
print(ans)