pfs = [i * i for i in range(1, 3163)]
p = [i for i in range(0, 10000001)]
for i in range(1, 10000001):
    if p[i] == i:
        for j in pfs:
            if i * j > 10000000:
                break
            p[i * j] = i


def main(n):
    if n < 1:
        n = 1
    t = n
    for case_id in range(t):
        k = (case_id % 10) + 1
        length = (case_id % 20) + 1
        base = (case_id * 12345) % 1000 + 2
        zc = [base + i for i in range(length)]
        s = [p[zc[i]] for i in range(0, len(zc))]
        dp = [length] * (k + 1)
        dp[0] = 1
        ys = [{}] * (length + 1)
        for i in range(0, len(s)):
            for j in range(k, -1, -1):
                if dp[j] == length:
                    continue
                if ys[j].get(s[i], -1) != -1:
                    if j < k and dp[j] < dp[j + 1]:
                        dp[j + 1] = dp[j]
                        ys[j + 1] = ys[j]
                    dp[j] += 1
                    ys[j] = {}
                ys[j][s[i]] = 1
        print(min(dp))


if __name__ == "__main__":
    main(5)