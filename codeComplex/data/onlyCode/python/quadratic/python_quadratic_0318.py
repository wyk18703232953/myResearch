#=============================================================================
# @abhi_admin    FB UserId: abhiavisekkr     Email Id: abhiavisekkr@gmail.com
#=============================================================================
#------------------------------Dependencies-----------------------------------
#import sys
#import math
#import cmath
#import array
#import string
#import functools #for .reduce()
#import itertools 


#def get_s(): return sys.stdin.readline().strip() 
#def get_i(): return map(int, sys.stdin.readline().strip().split())


#=============================================================================
#----------------------------Keep-Calm-and-Code-------------------------------
#=============================================================================




n, k = map(int, input().split())
arr = list(map(int, input().split()))

rsum = [0]
maxx = 0.0

for i in range(n): rsum.append(rsum[-1] + arr[i])
#print(rsum)

for ki in range(k, n+1):
    for i in range(n-ki+1):
        tot = 0
        #print(i+ki, i)
        avg = (rsum[i+ki] - rsum[i])/ki
        #print(avg)
        maxx = max(maxx, avg)
print(maxx)



#=============================================================================
#-----------------------------ADMIN-ABHI-SHAKE--------------------------------
#=============================================================================