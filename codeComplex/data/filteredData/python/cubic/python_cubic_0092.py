def main(n):
    # Generate deterministic data based on n
    # n: number of users / length of c, f arrays
    # k: fixed small constant to control DP width
    if n <= 0:
        # print(0)
        pass
        return

    k = 5
    c = [(i % (n // 2 + 1)) + 1 for i in range(n)]
    f = [(i * 2) % (n // 2 + 1) + 1 for i in range(n)]
    h = [i * i for i in range(1, k + 1)]

    cnt = {}
    for i in c:
        cnt[i] = cnt.get(i, 0) + 1
    likecolor = {}
    for i in range(n):
        likecolor.setdefault(f[i], []).append(i)
        cnt[f[i]] = cnt.get(f[i], 0)
    ans = 0
    for key, v in likecolor.items():
        n1 = len(v)
        if cnt[key] >= n1 * k:
            ans += n1 * h[k - 1]
            continue
        dp = [[-float("INF")] * (cnt[key] + 1) for _ in range(n1 + 1)]
        dp[0][0] = 0
        for i in range(n1):
            j = i + 1
            for e in range(cnt[key] + 1):
                if dp[i][e] > dp[j][e]:
                    dp[j][e] = dp[i][e]
                upper = min(cnt[key] + 1, e + k + 1)
                for w in range(e + 1, upper):
                    val = dp[i][e] + h[w - e - 1]
                    if val > dp[j][w]:
                        dp[j][w] = val
        ans += dp[n1][cnt[key]]
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)