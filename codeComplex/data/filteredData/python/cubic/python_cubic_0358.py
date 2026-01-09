import math
from collections import Counter, defaultdict
from bisect import insort

max_n = 10**7 + 1
spf = [i for i in range(max_n)]

for i in range(4, max_n, 2):
    spf[i] = 2

for i in range(3, math.isqrt(max_n) + 1):
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


def solve_one_case(n, k, a):
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
                val = dp[i][y] + 1
                if val < dp[end][x + y]:
                    dp[end][x + y] = val

    return dp[n][k]


def deterministic_case_params(n):
    if n < 1:
        n = 1
    max_n_local = 2000
    if n > max_n_local:
        n = max_n_local
    t = (n % 5) + 1
    base_len = max(1, n // t)
    cases = []
    for i in range(t):
        length = base_len + (i % 3)
        length = max(1, length)
        k = i % 5
        cases.append((length, k))
    return t, cases


def build_array(length, case_index):
    # deterministic construction: small numbers with some structure
    a = [(i + 1) * (case_index + 2) for i in range(length)]
    # add some repeated structure via modular arithmetic
    for i in range(length):
        val = a[i]
        if i % 4 == 0:
            val = val * val
        elif i % 4 == 1:
            val = val * (i + 3)
        elif i % 4 == 2:
            val = val * (i // 2 + 2)

        else:
            val = val * (case_index + 3)
        if val >= max_n:
            val = (val % (max_n - 1)) + 1
        if val == 0:
            val = 1
        a[i] = val
    return a


def main(n):
    t, cases = deterministic_case_params(n)
    results = []
    for idx in range(t):
        length, k = cases[idx]
        a = build_array(length, idx)
        res = solve_one_case(length, k, a)
        results.append(res)
    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    main(1000)