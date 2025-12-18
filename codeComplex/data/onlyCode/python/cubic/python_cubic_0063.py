# -*- coding: utf-8 -*-

s = input()
n,m = len(s),0

for i in range(n-1):
    for j in range(i,n+1):
        if len(s[i:j]) > m and s[i:j] in s[i+1:n]: m = len(s[i:j])
    
print(m)
