pfs = [i * i for i in range(1, 3163)]
p = [i for i in range(0, 10000001)]
for i in range(1, 10000001):
    if p[i] == i:
        for j in pfs:
            if i * j > 10000000:
                break
            p[i * j] = i


def main(n):
    # n controls: number of test cases and size of each test
    # Define number of test cases t and parameters per test deterministically from n
    if n <= 0:
        return
    t = max(1, n // 10)
    tests = []

    for case_id in range(t):
        # For each test case, derive n_i (length of array) and k_i from n and case_id
        ni = max(1, (n + case_id) % 1000 + 1)
        ki = max(1, (n // (case_id + 1)) % ni)
        # Build zc list deterministically using simple arithmetic and ensuring bounds
        zc = []
        base = n + case_id * 7
        for i in range(ni):
            v = (base + i * (case_id + 3)) % 10000000 + 1
            zc.append(v)
        tests.append((ni, ki, zc))

    for ni, k, zc in tests:
        s = [p[zc[i]] for i in range(0, len(zc))]
        dp = [ni] * (k + 1)
        dp[0] = 1
        ys = [{} for _ in range(ni + 1)]
        for i in range(0, len(s)):
            for j in range(k, -1, -1):
                if dp[j] == ni:
                    continue
                if ys[j].get(s[i], -1) != -1:
                    if j < k and dp[j] < dp[j + 1]:
                        dp[j + 1] = dp[j]
                        ys[j + 1] = ys[j]
                    dp[j] += 1
                    ys[j] = {}
                ys[j][s[i]] = 1
        # print(min(dp))
        pass
if __name__ == "__main__":
    main(1000)