# https://codeforces.com/problemset/problem/1004/A
# 900

n, k = map(int, input().split())
l = list(map(int, input().split()))

o = 2
for i in range(n):
    if i+1 == n:
        break

    d = abs(l[i] - l[i+1]) / k
    if d ==  2:
        o += 1
    elif d > 2:
        o += 2

print(o)