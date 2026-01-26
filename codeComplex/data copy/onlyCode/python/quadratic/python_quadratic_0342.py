n = int(input())
s = list(str(input()))
t = list(str(input()))
 
from collections import Counter
cs = Counter(s)
ct = Counter(t)
if cs != ct:
    print(-1)
    exit()
 
xs = [[] for _ in range(26)]
xt = [[] for _ in range(26)]
for i in range(n):
    j = ord(s[i])-ord('a')
    xs[j].append(i)
 
for i in range(n):
    j = ord(t[i])-ord('a')
    xt[j].append(i)
 
x = [-1]*n
for i in range(26):
    for j, k in zip(xs[i], xt[i]):
        x[j] = k
 
ans = []
for i in range(n):
    for j in reversed(range(i+1, n)):
        if x[j-1] > x[j]:
            x[j-1], x[j] = x[j], x[j-1]
            ans.append(j)
print(len(ans))
print(*ans)