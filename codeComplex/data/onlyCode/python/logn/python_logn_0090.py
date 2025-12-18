import sys
# from math import log2,floor,ceil,sqrt
# import bisect
# from collections import deque

# from types import GeneratorType
# def bootstrap(func, stack=[]):
#     def wrapped_function(*args, **kwargs):
#         if stack:
#             return func(*args, **kwargs)
#         else:
#             call = func(*args, **kwargs)
#             while True:
#                 if type(call) is GeneratorType:
#                     stack.append(call)
#                     call = next(call)
#                 else:
#                     stack.pop()
#                     if not stack:
#                         break
#                     call = stack[-1].send(call)
#             return call
#     return wrapped_function

Ri = lambda : [int(x) for x in sys.stdin.readline().split()]
ri = lambda : sys.stdin.readline().strip()

def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
INF = 10 ** 18
MOD = 10**8
N = 5*10**6

def solve(n):
    arr = []
    while n> 0:
        arr.append(n%2)
        n=n//2
    return arr

l,r = Ri()
arrl = solve(l)
arrr = solve(r)
if len(arrr) > len(arrl):
    ans = (1<<len(arrr))-1
    print(ans)
else:
    ind = -1
    for i in range(len(arrr)-1,-1,-1):
        if arrr[i] != arrl[i]:
            ind = i
            break
    if ind == -1:
        print(0)
    else:
        ans = (1 << (ind+1)) -1
        print(ans)


