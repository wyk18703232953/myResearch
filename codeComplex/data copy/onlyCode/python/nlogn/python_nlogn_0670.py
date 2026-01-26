from collections import deque
# classic top sort
def top_sort():
    global dag, top, g, n
    q = deque()
    cnt = 0

    for i in range(1, n+1):
        if not dag[i]:
            q.append(i)

    while len(q):
        u = q.popleft()
        cnt += 1
        top[u] = cnt
        for to in g[u]:
            dag[to] -= 1
            if dag[to] == 0:
                q.append(to)
    return cnt == n

# creates graph with edges w < mid
def check(mid):
    global n, m, g, u, v, c, dag
    for i in range(1, n+1):
        g[i].clear()
        dag[i] = 0
    for i in range(1, m+1):
        if c[i] > mid:
            g[u[i]].append(v[i])
            dag[v[i]] += 1
    return top_sort()


def input_t():
    return [int(x) for x in input().split()]


MAX = int(10e5 + 42)
n, m = input_t()
r = 0
u, v, c = [0] * MAX, [0] * MAX, [0] * MAX
g, dag, top = [[]  for _ in range(MAX)], [0] * MAX, [0] * MAX
cnt = 0

for i in range(1, m + 1):
    u[i], v[i], c[i] = input_t()
    r = max(r, c[i])

l = 0

# b search
while l < r:
    mid = (l+r) >> 1
    if check(mid):
        r = mid
    else:
        l = mid + 1

check(l)
for i in range(1, m+1):
    if c[i] <= l and top[v[i]] < top[u[i]]:
        cnt += 1
print(f"{l} {cnt}")
for i in range(1, m+1):
    if c[i] <= l and top[v[i]] < top[u[i]]:
        print(i, end=" ")

