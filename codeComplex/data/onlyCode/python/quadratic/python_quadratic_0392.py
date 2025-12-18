from math import *
n,m = map(int,input().split())
li = [[j for j in input()] for i in range(n)]
min1=inf
min2=inf
max1=-inf
max2=-inf
for i in range(n):
    for j in range(m):
        if li[i][j] == "B":
            min1 = min(min1,i)
            min2 = min(min2, j)
            max1 = max(max1, i)
            max2 = max(max2, j)
print((min1+max1)//2+1,(min2+max2)//2+1)