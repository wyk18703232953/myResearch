import math


def main(n):
    # Map n to original parameters:
    # n -> number of items (n_items)
    # m -> max number of chosen items (<= n_items)
    # k -> number of bonus rules
    n_items = max(1, n)
    m = max(1, n_items // 2)
    k = n_items * 2

    # Deterministic generation of a (length n_items)
    # Example: a[i] = (i % 7) + 0.5
    a = [float((i % 7) + 1) * 0.1 + float(i % 5) for i in range(n_items)]

    # Deterministic generation of add matrix (size (n_items+1) x n_items)
    add = [[0.0] * n_items for _ in range(n_items + 1)]
    for t in range(k):
        xi = (t % (n_items + 1)) + 1       # 1..n_items+1
        yi = (t * 2) % n_items + 1         # 1..n_items
        ci = (t * 3 + xi + yi) % 10        # some integer bonus
        add[xi - 1][yi - 1] = float(ci)

    minf = float('-inf')
    dp = [[minf] * (1 << n_items) for _ in range(n_items + 1)]
    dp[n_items][0] = 0.0

    for bitset in range(1 << n_items):
        if bin(bitset).count('1') >= m:
            continue
        for i in range(n_items + 1):
            if dp[i][bitset] == minf:
                continue
            base = dp[i][bitset]
            for j in range(n_items):
                if (bitset >> j) & 1:
                    continue
                nb = bitset | (1 << j)
                val = base + a[j] + add[i][j]
                if val > dp[j][nb]:
                    dp[j][nb] = val

    ans = max(max(row) for row in dp)
    print(int(ans + 1e-7))


if __name__ == "__main__":
    main(4)