from math import *
a,r = map(int,input().split())
x = list(map(int,input().split()))
y = [0]*a
for i in range(a):
    h = r
    for j in range(i):
        if abs(x[i]-x[j])<=2*r:
            h = max(h,sqrt((2*r)**2 - (x[i]-x[j])**2)+y[j])
    y[i] = h
    print(h, end = " ")
