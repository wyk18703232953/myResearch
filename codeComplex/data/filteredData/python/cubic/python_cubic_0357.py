pfs = [i * i for i in range(1, 3163)]
p = [i for i in range(0, 10000001)]
for i in range(1, 10000001):
    if p[i] == i:
        for j in pfs:
            if i * j > 10000000:
                break
            p[i * j] = i


def run_single_case(n, k, zc):
    s = [p[zc[i]] for i in range(0, len(zc))]
    dp = [n] * (k + 1)
    dp[0] = 1
    ys = [{}] * (n + 1)
    for i in range(0, len(s)):
        for j in range(k, -1, -1):
            if dp[j] == n:
                continue
            if ys[j].get(s[i], -1) != -1:
                if j < k and dp[j] < dp[j + 1]:
                    dp[j + 1] = dp[j]
                    ys[j + 1] = ys[j]
                dp[j] += 1
                ys[j] = {}
            ys[j][s[i]] = 1
    return min(dp)


def generate_test_cases(n):
    t = n
    cases = []
    for case_id in range(1, t + 1):
        k = max(1, case_id % n)
        length = max(1, n)
        base = 2 * case_id
        zc = [base * (i + 1) for i in range(length)]
        zc = [min(10000000, max(1, v)) for v in zc]
        cases.append((length, k, zc))
    return t, cases


def main(n):
    t, cases = generate_test_cases(n)
    results = []
    for length, k, zc in cases:
        res = run_single_case(length, k, zc)
        results.append(res)
    for v in results:
        # print(v)
        pass
if __name__ == "__main__":
    main(5)