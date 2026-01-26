query = input().split()

n = int(query[0])
k = int(query[1])
import math

'''for ii in range(n):
    temp = (ii+1)*(ii+2)/2 - k
    for jj in range(n):
        if temp - jj == k and (ii + jj) + 1 == n:
            print(jj)
            flag = 0
            break
    if flag == 0:
        break'''

temp = 2* (k + n)

m = (-3 + math.sqrt(9 + 4*temp))/2

print(int(n-m))
'''if flag == 1:
    for i in range(n):
        if (i+1)*(i+2)/2 + i + 1 == n:
            print(int((i+1)*(i+2)/2))
            break'''
