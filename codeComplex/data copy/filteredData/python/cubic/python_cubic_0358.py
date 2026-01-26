import os
from math import sqrt, ceil
from collections import Counter, defaultdict
from bisect import insort

max_n = 10**7 + 1
spf = [i for i in range(max_n)]

for i in range(4, max_n, 2):
    spf[i] = 2

for i in range(3, ceil(sqrt(max_n))):
    if spf[i] == i:
        for j in range(i * i, max_n, i):
            if spf[j] == j:
                spf[j] = i


def f(x):
    c = Counter()
    ans = 1
    while x != 1:
        c[spf[x]] += 1
        x //= spf[x]
    for i in c:
        if c[i] % 2 == 1:
            ans *= i
    return ans


def run_case(n, k, a):
    for i in range(n):
        a[i] = f(a[i])
    dp_depth = [[n for _ in range(k + 1)] for _ in range(n)]
    recent = [n for _ in range(k + 1)]
    closest = defaultdict(lambda: -1)
    for i in range(n - 1, -1, -1):
        if closest[a[i]] >= 0:
            insort(recent, closest[a[i]])
            recent.pop()
        dp_depth[i] = recent.copy()
        closest[a[i]] = i
    dp = [[i for _ in range(k + 1)] for i in range(n + 1)]
    dp[0] = [0 for _ in range(k + 1)]
    for i in range(n):
        for x in range(k + 1):
            end = dp_depth[i][x]
            for y in range(k - x + 1):
                dp[end][x + y] = min(dp[end][x + y], dp[i][y] + 1)
    return dp[n][k]


def generate_case(case_idx, n):
    # Map global n to per-case size deterministically
    # Let number of cases T = min(n, 10)
    T = min(n, 10)
    base_len = max(1, n // T)
    extra = n % T
    # Per-case length
    if case_idx < extra:
        length = base_len + 1
    else:
        length = base_len
    # Bound length to a reasonable size
    length = max(1, min(length, 2000))
    # Choose k based on length
    k = max(0, min(length, case_idx % (length + 1)))
    # Build array a deterministically, values >= 1
    a = [( (case_idx + 1) * (i + 1) ) % (10**7) + 1 for i in range(length)]
    return length, k, a


def main(n):
    # n controls overall total input size
    if n <= 0:
        return
    T = min(n, 10)
    results = []
    for t in range(T):
        length, k, a = generate_case(t, n)
        res = run_case(length, k, a)
        results.append(str(res))
    os.write(1, ("\n".join(results) + "\n").encode())


if __name__ == "__main__":
    main(1000)