# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 23:11:30 2020

LCM Challenge

@author --> yashodeep
@Link --> https://codeforces.com/problemset/problem/235/A
@status --> Accepted in first attempt
"""
n = int(input())
ans = 1
if n == 1:
    ans = 1
elif n == 2:
    ans = 2
elif n == 3:
    ans = 6
elif n%2 == 0:
    if n%3 == 0:
        ans = (n-1)*(n-2)*(n-3)
    else:
        ans = n*(n-1)*(n-3)
else:
    ans = n*(n-1)*(n-2)

print(ans)