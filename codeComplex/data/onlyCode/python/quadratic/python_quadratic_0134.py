import bisect
import math
import itertools
import sys

# import sys.stdout.flush() use for interactive problems
alpha = 'abcdefghijklmnopqrstuvwxyz'
inf = 1e17


# Max = 10**6
# primes = []
# prime = [True for i in range(10**6+1)]
# p = 2
# while (p * p <= Max+1):
#
#     # If prime[p] is not
#     # changed, then it is a prime
#     if (prime[p] == True):
#
#         # Update all multiples of p
#         for i in range(p * p, Max+1, p):
#             prime[i] = False
#     p += 1
#
# for p in range(2, Max+1):
#     if prime[p]:
#         primes.append(p)
def calc1(grid):
    l = len(grid)
    cnt = 0
    for i in range(l):
        for j in range(l):
            if (i+j) % 2 and grid[i][j]:
                cnt += 1
            if (i+j) % 2 == 0 and grid[i][j] == 0:
                cnt += 1
    return cnt

def calc2(grid):
    l = len(grid)
    cnt = 0
    for i in range(l):
        for j in range(l):
            if (i+j) % 2 and grid[i][j] == 0:
                cnt += 1
            if (i+j) % 2 == 0 and grid[i][j]:
                cnt += 1
    return cnt
def solve(n,grids):
    one = []
    zero = []
    for grid in grids:
        one.append(calc1(grid))
        zero.append(calc2(grid))
    take = [3,5,6,9,10,12]
    answer = inf
    for mask in range(16):
        cnt = 0
        if mask not in take:
            continue
        if mask in take:
            if mask & 1:
                cnt += one[3]
                pass
            else:
                cnt += zero[3]
                pass
            if mask & 2:
                cnt += one[2]
                pass
            else:
                cnt += zero[2]
                pass
            if mask & 4:
                cnt += one[1]
                pass
            else:
                cnt += zero[1]
                pass
            if mask & 8:
                cnt += one[0]
                pass
            else:
                cnt += zero[0]
                pass
        answer = min(answer,cnt)
    return answer

t = 1#int(input())
ans = []
for _ in range(t):
    n = int(input())
    #n, u, r, d, l = map(int, input().split())
    #a,b = map(int, input().split())
    # s = input()
    # arr = list(input())
    # arr = [int(x) for x in input().split()]
    # c = [int(x) for x in input().split()]

    # b = [int(x) for x in input().split()]
    # s = input()
    # t = input()
    grids = []
    for i in range(4):
        grid = []
        for j in range(n):
            arr = list(map(int,list(input())))
            grid.append(arr)
        if i != 3:
            s = input()
        grids.append(grid)
    # options = [int(x) for x in input().split()]
    """ladders = []
    for j in range(l):
        ladders.append([int(x) for x in input().split()])"""
    """queries = []
    for j in range(q):
        queries.append(list(map(int, input().split())))"""
    # s = list(input())
    # start,end = map(int,input().split())

    ans.append(solve(n,grids))

for test in ans:
    print(test)