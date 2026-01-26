#!/usr/bin/env python3
import io
import os
import sys

input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

def prdbg(*args, **kwargs):
    print(*args, **kwargs)
    pass

def get_str():
    return input().decode().strip()

def rint():
    return map(int, input().split())

def oint():
    return int(input())

def valid(i1,i2,i3):
    if (i1+i2+i3)%2 or (i1 < 0 or i2 < 0 or i3 < 0) or i3 > i1 + i2\
            or i2 > i1 + i3 or i1 > i2 + i3:
        return False
    return True

def dfs(i1,i2,i3):
    #if not valid(i1, i2, i3):
    if (i1 + i2 + i3) % 2 or (i1 < 0 or i2 < 0 or i3 < 0) or i3 > i1 + i2 \
                or i2 > i1 + i3 or i1 > i2 + i3:
        return -2
    if dp[i1][i2][i3] != -1:
        return dp[i1][i2][i3]
    ret1 = dfs(i1-1, i2-1, i3)
    if ret1 >= 0 :
        ret1 += a1[i1]*a2[i2]
    ret2 = dfs(i1-1, i2, i3-1)
    if ret2 >= 0:
        ret2 += a1[i1]*a3[i3]
    ret3 = dfs(i1, i2-1, i3-1)
    if ret3 >= 0:
        ret3 += a2[i2]*a3[i3]
    ret = max(ret1, ret2, ret3)
    dp[i1][i2][i3] = ret
    return ret

n1, n2, n3 = rint()
a1, a2, a3 = list(rint()), list(rint()), list(rint())
a1.sort(reverse=True)
a2.sort(reverse=True)
a3.sort(reverse=True)
a1 = [0] + a1
a2 = [0] + a2
a3 = [0] + a3
n1 += 1
n2 += 1
n3 += 1

dp = [[[-1 for i3 in range(n3)] for i2 in range(n2)] for i1 in range(n1)]
dp[1][1][0] = a1[1]*a2[1]
dp[1][0][1] = a1[1]*a3[1]
dp[0][1][1] = a2[1]*a3[1]
dp[0][0][0] = -2

for i1 in range(n1):
    for i2 in range(n2):
        for i3 in range(n3):
            dfs(i1, i2, i3)
ans = -1
for i1 in range(n1):
    for i2 in range(n2):
        for i3 in range(n3):
            ans = max(ans, dp[i1][i2][i3])
#print(a1,a2,a3)
print(ans)
