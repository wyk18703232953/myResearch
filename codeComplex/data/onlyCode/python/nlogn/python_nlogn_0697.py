import math,sys,bisect,heapq,os
from collections import defaultdict,Counter,deque
from itertools import groupby,accumulate
from functools import lru_cache
#sys.setrecursionlimit(200000000)
pr = lambda x:    x
def input(): return sys.stdin.readline().rstrip('\r\n')
#input = iter(sys.stdin.buffer.read().decode().splitlines()).__next__
aj = lambda: list(map(int, input().split()))
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
#MOD = 1000000000 + 7
def Y(c):  print(["NO","YES"][c])
def y(c):  print(["no","yes"][c])
def Yy(c):  print(["No","Yes"][c])

def solve():
    n, = aj()
    A = aj()
    if A.count(0) >= 2:
        print('cslnb')
    elif n == 1:
        if A[0]%2:
            print('sjfnb')
        else:
            print('cslnb')
    else:
        g2 = 0;flag = 1
        C = Counter(A)
        for i in C.keys():
            if C[i] >= 3:
                flag = 0
            if C[i] == 2 and C[i-1] >= 1:
                flag = 0
            if C[i] == 2:
                g2 += 1
        if g2 >= 2:
            flag = 0
        if not flag:
            print('cslnb')
        else:
            movescount = 0
            A.sort()
            for ii,i in enumerate(A):
                movescount += i - ii
            if movescount % 2 == 0:
                print('cslnb')
            else:
                print('sjfnb')



try:
    #os.system("online_judge.py")
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
    from aj import *
except:
    pass

solve()