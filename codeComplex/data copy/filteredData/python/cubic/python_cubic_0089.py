from collections import Counter

def main(n):
    if n <= 0:
        return 0

    # Define k based on n (bounded to keep DP size reasonable for experiments)
    k = max(1, min(10, n // 5))

    # Let the number of items be n
    num_items = n

    # Construct colors c and favorites f with some repeated structure
    # Use small color IDs so counters have overlaps
    num_colors = max(1, min(10, n // 3))
    c = [(i % num_colors) + 1 for i in range(num_items)]
    f = [((i * 2) % num_colors) + 1 for i in range(num_items)]

    # h has length at least k+1 (index 0..k); build deterministically
    h_len = k + 1
    h = [0] + [((i * i) // 2 + i) % (n + 5) + 1 for i in range(1, h_len)]

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
                    dp[x][ki + s] = max(dp[x][ki + s], dp[x - 1][s] + (h[ki] if ki < len(h) else 0))
        ans += dp[m][t]
    return ans

if __name__ == "__main__":
    # Example deterministic call; change n to scale input size for experiments
    result = main(20)
    print(result)