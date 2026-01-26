from collections import defaultdict

n = int(raw_input())
t = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, raw_input().split())
    t[u].append(v)
    t[v].append(u)
a = list(map(int, raw_input().split()))
o = {a_: i for i, a_ in enumerate(a)}

i = 0
q = [1]
lv = {1: 0}
par = {1: 1}
while i < len(q):
    u = q[i]
    i += 1
    for v in t[u]:
        if v not in lv:
            lv[v] = lv[u] + 1
            q.append(v)
            par[v] = u

depths = defaultdict(list)
for x in a:
    depths[lv[x]].append(o[par[x]])

ans = a[0] == 1
if ans:
    for d in depths.values():
        if not all(d[i] <= d[i + 1] for i in range(len(d) - 1)):
            ans = False
            break

if ans:
    l = [lv[x] for x in a]
    ans = all(l[i] <= l[i + 1] for i in range(len(l) - 1))

print(('No', 'Yes')[ans])
