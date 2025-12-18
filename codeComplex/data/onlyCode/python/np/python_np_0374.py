import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

INF = 10**9

n, m = [int(item) for item in input().split()]
s = input().rstrip()

# Calculate adjacent count in subset
adj_in_subset = [0] * (1 << m)
ord_a = ord("a")
for c1, c2 in zip(s, s[1:]):
    c1 = ord(c1) - ord_a
    c2 = ord(c2) - ord_a
    if c1 != c2:
        adj_in_subset[(1 << c1) + (1 << c2)] += 1
for i in range(m):
    for j in range(1 << m):
        if j & (1 << i):
            adj_in_subset[j] += adj_in_subset[j ^ (1 << i)]

total_adj = adj_in_subset[-1]
dp = [INF] * (1 << m)
dp[0] = 0

for i in range(1 << m):
    for j in range(m):
        if i & 1 << j:
            continue
        cost = total_adj - adj_in_subset[i] - adj_in_subset[~i]
        dp[i | (1 << j)] = min(dp[i | (1 << j)], dp[i] + cost)
print(dp[-1])