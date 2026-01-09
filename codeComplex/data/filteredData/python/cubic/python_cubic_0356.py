pfs = [i * i for i in range(1, 3163)]
p = [i for i in range(0, 10000001)]
for i in range(1, 10000001):
    if p[i] == i:
        for j in pfs:
            if i * j > 10000000:
                break
            p[i * j] = i

def main(n):
    t = n
    results = []
    for case in range(t):
        k = n % 10 + 1
        length = n + case
        if length <= 0:
            length = 1
        zc = [((case + 1) * (i + 1)) % 10000000 + 1 for i in range(length)]
        s = [p[zc[i]] for i in range(0, len(zc))]
        dp = [n] * (k + 1)
        dp[0] = 1
        ys = [{} for _ in range(n + 1)]
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
        results.append(min(dp))
    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    main(5)