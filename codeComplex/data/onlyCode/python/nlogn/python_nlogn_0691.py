n, m = map(int, input().split())
b = list(map(int, input().split()))
g = list(map(int, input().split()))
Sum = 0
for j in range(n):
    Sum+=b[j]*m
b.sort()
for i in range(m):
    Sum+=max(0, g[i]-b[-1])
if min(g)<max(b): print(-1)
elif min(g)==max(b): print(Sum)
else: Sum+=b[-1]-b[-2]; print(Sum)