pfs = [i * i for i in range(1, 3163)]
p = [i for i in range(0, 10000001)]
for i in range(1, 10000001):
    if p[i] == i:
        for j in pfs:
            if i * j > 10000000:
                break
            p[i * j] = i

def run_case(n, k, zc):
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

def main(n):
    t = max(1, n)
    results = []
    for case_id in range(1, t + 1):
        k = case_id % 10 + 1
        length = case_id % 20 + 1
        length = min(length, n + 1)
        zc = [((i + 1) * (case_id + 1)) % 10000000 + 1 for i in range(length)]
        res = run_case(length, k, zc)
        results.append(res)
        # print(res)
        pass
    return results

if __name__ == "__main__":
    main(3)