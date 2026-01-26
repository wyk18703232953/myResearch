pfs = [i * i for i in range(1, 3163)]
p = [i for i in range(0, 10000001)]
for i in range(1, 10000001):
    if p[i] == i:
        for j in pfs:
            if i * j > 10000000:
                break
            p[i * j] = i

def main(n):
    # 将 n 解释为数组 zc 的长度；k 取 n//2（至少为 1）
    if n <= 0:
        return
    k = n // 2
    if k == 0:
        k = 1
    # 生成确定性的 zc：在合法范围内循环使用 1..10000000
    zc = [(i % 10000000) + 1 for i in range(1, n + 1)]

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
    # print(min(dp))
    pass
if __name__ == "__main__":
    main(10)