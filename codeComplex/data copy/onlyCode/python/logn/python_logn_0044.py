"""
2 3 1 2
"""


import sys
import bisect
import heapq
import math

INF = 10**9+7
sys.setrecursionlimit(INF)

def fi():
    return int(sys.stdin.readline())

def fi2():
    return map(int, sys.stdin.readline().split())

def fi3():
    return sys.stdin.readline().rstrip()

def fo(*args):
    for s in args:
        sys.stdout.write(str(s)+' ')
    sys.stdout.write('\n')
##    sys.stdout.flush()

def puts(*args):
    for s in args:
        sys.stdout.write(str(s))

##

def mask(n1):
    arr = []
    for i in range(64):
        arr.append(n1&1)
        n1 = n1 >> 1
    arr.reverse()
    return arr

def getn(mask):
    if sum(mask) == 0:
        return 0
    res = 0
    for i in range(63, -1, -1):
        res += (2*mask[i])**(63-i)
    return res





##
#main

n1, n2 = fi2()
m1 = mask(n1)
m2 = mask(n2)



sol = [0 for i in range(64)]

for i in range(64):
    if m1[i] != m2[i]:
        sol[i] = 1
        break
    
i += 1
for j in range(i, 64):
    sol[j] = 1

res = getn(sol)
fo(res)


            
                

            
        

    

