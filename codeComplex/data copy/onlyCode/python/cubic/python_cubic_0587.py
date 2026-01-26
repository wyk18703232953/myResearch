# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 08:45:24 2020

@author: Dark Soul
"""
def comp(a,b):
    x=len(a)
    s1=''
    s2=''
    for i in range(x):
        s1+=str(a[i])
        s2+=str(b[i])
    if s1>s2:
        return 1
    else:
        return 0
        
a=list(input(''))
b=list(input(''))
cnt=[0]*10
n=len(a)
m=len(b)
sol=''
for i in range(n):
    a[i]=int(a[i])
    cnt[a[i]]+=1

if n!=m:
    a.sort(reverse=True)
    for i in a:
        sol+=str(i)
    print(sol)
else:
    a.sort()
    
    for i in range(n):
        b[i]=int(b[i])
    for i in range(n-1):
        for j in range(i,n):
            if a[i]<a[j]:
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
                if comp(a,b):
                    temp=a[i]
                    a[i]=a[j]
                    a[j]=temp
                
    
    for i in a:
        sol+=str(i)
    print(sol)