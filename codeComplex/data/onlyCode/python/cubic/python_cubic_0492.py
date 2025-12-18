n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n-1)]

if k % 2 == 1:
    for i in range(n):
        print(*[-1]*m)
    exit()
k //= 2

INF = 10**18
dp = [[[INF]*(k+1) for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        dp[i][j][0] = 0

for v in range(1, k+1):
    for i in range(n):
        for j in range(m):
            now_h, now_w = i, j
            if i > 0:
                dp[i][j][v] = min(dp[i-1][j][v-1]+b[i-1][j], dp[i][j][v])
            if i < n-1:
                dp[i][j][v] = min(dp[i+1][j][v-1]+b[i][j], dp[i][j][v])
            if j > 0:
                dp[i][j][v] = min(dp[i][j-1][v-1]+a[i][j-1], dp[i][j][v])
            if j < m-1:
                dp[i][j][v] = min(dp[i][j+1][v-1]+a[i][j], dp[i][j][v])

for i in range(n):
    v = []
    for j in range(m):
        v.append(dp[i][j][k]*2)
    print(*v)

# class UnionFind():
#     def __init__(self, n):
#         self.n = n
#         self.parents = [-1] * n

#     def find(self, x):
#         if self.parents[x] < 0:
#             return x
#         else:
#             self.parents[x] = self.find(self.parents[x])
#             return self.parents[x]

#     def union(self, x, y):
#         x = self.find(x)
#         y = self.find(y)

#         if x == y:
#             return

#         if self.parents[x] > self.parents[y]:
#             x, y = y, x

#         self.parents[x] += self.parents[y]
#         self.parents[y] = x

#     def size(self, x):
#         return -self.parents[self.find(x)]

#     def same(self, x, y):
#         return self.find(x) == self.find(y)

#     def members(self, x):
#         root = self.find(x)
#         return [i for i in range(self.n) if self.find(i) == root]

#     def roots(self):
#         return [i for i, x in enumerate(self.parents) if x < 0]

#     def group_count(self):
#         return len(self.roots())

#     def all_group_members(self):
#         group_members = defaultdict(list)
#         for member in range(self.n):
#             group_members[self.find(member)].append(member)
#         return group_members

#     def __str__(self):
#         return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


# q = []
# heapq.heapify(q)
# path = [[] for _ in range(n*m)]
# for i in range(n):
#     a = list(map(int, input().split()))
#     for j in range(m - 1):
#         edge = (a[j], i*m+j, i*m+j+1)
#         heapq.heappush(q, edge)
# for i in range(n - 1):
#     a = list(map(int, input().split()))
#     for j in range(m):
#         edge = (a[j], i * m + j, m * (i + 1) + j)
#         heapq.heappush(q, edge)

# uf = UnionFind(n * m)

# path = [[] for _ in range(n*m)]

# while q:
#     edge = heapq.heappop(q)
#     cost, v1, v2 = edge
#     if uf.same(v1, v2):
#         continue
#     else:
#         uf.union(v1, v2)
#     path[v1].append((v2, cost))
#     path[v2].append((v1, cost))

# for i in path:
#     print(i)
# # print(path)
# exit()
