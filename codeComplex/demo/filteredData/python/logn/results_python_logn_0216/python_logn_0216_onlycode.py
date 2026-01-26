#Bhargey Mehta (Sophomore)
#DA-IICT, Gandhinagar
import sys, math, queue, bisect
#sys.stdin = open("input.txt", "r")
MOD = 10**9+7
sys.setrecursionlimit(1000000)

def ok(x):
    y = sum(map(int, list(str(x))))
    return x-y >= s

n, s = map(int, input().split())
l, h = 0, n
a = n
while l <= h:
    m = (l+h)>>1
    if ok(m):
        a = m-1
        h = m-1
    else:
        l = m+1
print(n-a)