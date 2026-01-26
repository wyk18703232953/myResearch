import sys

def main(n):
    # n controls the problem size: number of nodes
    if n <= 0:
        return
    # define m (subset size) as roughly half of n, at least 1
    m = max(1, n // 2)
    # define k (number of edges with extra weight)
    k = n * n // 4

    # deterministic generation of a[i] as floats
    # example: a[i] = (i % 7) + 0.5 * (i % 3)
    a = [float((i % 7) + 0.5 * (i % 3)) for i in range(n)]

    # deterministic generation of tree matrix
    tree = [[0.0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if cnt < k and i != j:
                # deterministic weight; can be negative or positive
                tree[i][j] = float(((i + 1) * (j + 3)) % 11 - 5)
                cnt += 1
            if cnt >= k:
                break
        if cnt >= k:
            break

    # build powers of two list po such that len(po) == n
    po = [1]
    while len(po) != n:
        po.append(po[-1] * 2)

    dp = [[0.0] * (po[-1] * 2) for _ in range(n)]
    for i in range(n):
        dp[i][po[i]] = a[i]

    limit = po[-1] * 2
    for mask in range(limit):
        for j in range(n):
            if mask & po[j]:
                base = dp[j][mask]
                if base == 0.0 and mask != po[j]:
                    continue
                for k_idx in range(n):
                    if not (mask & po[k_idx]):
                        nxt = mask + po[k_idx]
                        val = base + a[k_idx] + tree[j][k_idx]
                        if val > dp[k_idx][nxt]:
                            dp[k_idx][nxt] = val

    ma = 0.0
    for mask in range(limit):
        if bin(mask).count("1") == m:
            for j in range(n):
                if dp[j][mask] > ma:
                    ma = dp[j][mask]

    print(int(ma))


if __name__ == "__main__":
    # example deterministic call
    main(10)