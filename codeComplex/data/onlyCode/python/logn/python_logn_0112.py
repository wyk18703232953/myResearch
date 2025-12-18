# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 22:59:16 2020

@author: Dark Soul
"""
import math
[l,r]=list(map(int,input().split()))
l=l^r
if l:
    l=int(math.log(l,2))
    l=(1<<(l+1))-1
    print(l)
else:
    print(0)