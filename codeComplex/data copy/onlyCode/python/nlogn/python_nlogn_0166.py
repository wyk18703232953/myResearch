import sys
stdin=sys.stdin

ip=lambda: int(sp())
fp=lambda: float(sp())
lp=lambda:list(map(int,stdin.readline().split()))
sp=lambda:stdin.readline().rstrip()
Yp=lambda:print('Yes')
Np=lambda:print('No')

N = ip()
L = []
for _ in range(N):
    x,w = lp()
    L.append([x-w,x+w])
L.sort(reverse=True)
ans = 0
edge = 1<<40
for i in range(N):
    if L[i][1] <= edge:
        edge = L[i][0]
        ans += 1
print(ans)