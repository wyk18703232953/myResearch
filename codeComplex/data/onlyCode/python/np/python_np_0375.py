n, m = map(int, input().split())
a = list(map(str, input().strip()))

dp = [10 ** 10] * (1 << 20)
cnt = [0] * (1 << 20)


def get(x):
    return 1 << (ord(x) - ord('a'))


for i, v in enumerate(a):
    if i:
        cnt[get(a[i]) | get(a[i - 1])] += 1

for i in range(m):
    for j in range(1 << m):
        if (1 << i) & j:
            cnt[j] += cnt[j ^ (1 << i)]
            # print(bin(j), bin(j ^ 1 << i), cnt[j])

# for i in range(1 << m):
#     for j in range(m):
#         if not i & (1 << j):
#             cnt[i | (1 << j)] += cnt[i]
#             print(bin(i | (1 << j)), bin(i), cnt[i | 1 << j])

dp[0] = 0

for i in range(1 << m):
    for j in range(m):
        if not i & (1 << j):
            dp[i | (1 << j)] = min(dp[i | (1 << j)],
                                   dp[i] + n - 1 - cnt[i | (1 << j)] - cnt[(1 << m) - 1 - (i | (1 << j))])
print(dp[(1 << m) - 1])
