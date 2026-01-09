from collections import Counter

def main(n):
    # Ensure n is at least 1
    if n <= 0:
        n = 1

    # Define parameters based on n
    k = max(1, n // 5)
    m_unique = max(1, n // 4)

    # Build colors list c: length n, values in [1, m_unique]
    c = [(i % m_unique) + 1 for i in range(n)]

    # Build favorite list f: length n, same value domain as c
    f = [((i * 2) % m_unique) + 1 for i in range(n)]

    # Build happiness array h of length k + 1, 1-based in original code
    # h[0] is dummy; h[1..k] are deterministic values
    h = [0] + [i * i for i in range(1, k + 1)]

    cnt_all = Counter(c)
    cnt_fav = Counter(f)

    ans = 0
    for fi in cnt_fav:
        if fi not in cnt_all:
            continue
        m = cnt_fav[fi]
        t = min(cnt_all[fi], m * k)
        dp = [[0] * (t + 1) for _ in range(m + 1)]
        for x in range(1, m + 1):
            for s in range(0, t + 1):
                for ki in range(0, k + 1):
                    if ki + s > t:
                        break
                    dp[x][ki + s] = max(dp[x][ki + s], dp[x - 1][s] + h[ki])
        ans += dp[m][t]

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)