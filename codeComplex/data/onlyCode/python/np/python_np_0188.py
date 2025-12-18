# -*- coding: utf-8 -*-
"""
Created on Sun May 26 12:02:26 2019

@author: avina
"""

N,L,H,d = map(int, input().split())

l = list(map(int, input().split()))
e = 0
for i in range(1 << N ):
    k = []
    for j in range(N):
        if i >> j & 1:
            k.append(l[j])
    if len(k)>0:
        maz = max(k)
        mins = min(k)
        sums = sum(k)
        if sums >= L and sums <=H:
            if maz - mins >=d:
                e+=1
print(e)