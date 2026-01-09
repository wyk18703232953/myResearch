def main(n):
    cost = [0] + [i + 1 for i in range(4)]
    rows, cols = 4, n
    a = []
    for y in range(rows):
        row = []
        for x in range(cols):
            row.append('.' if (x + y) % 2 == 0 else '#')
        a.append(''.join(row))

    mask = [0, 1, 51, 1911]
    inf, bs_size, full_bit = 10**9, 1 << 12, (1 << 12) - 1
    dp = [[inf] * bs_size for _ in range(4 * n + 1)]
    dp[0][0] = 0

    for i in range(4 * n):
        y, x = i & 3, i >> 2
        is_dot = 1 if a[y][x] == '.' else 0

        for bitset in range(bs_size):
            cur = dp[i][bitset]
            if cur == inf:
                continue

            if y == 0:
                nxt = cur + cost[4]
                if dp[i + 4][full_bit] > nxt:
                    dp[i + 4][full_bit] = nxt

            if (is_dot | (bitset & 1)):
                if dp[i + 1][bitset >> 1] > cur:
                    dp[i + 1][bitset >> 1] = cur

            for k in range(1, min(4 - y, 3) + 1):
                nb = bitset | mask[k]
                nxt = cur + cost[k]
                if dp[i][nb] > nxt:
                    dp[i][nb] = nxt

    result = min(dp[4 * n])
    return result


if __name__ == "__main__":
    # print(main(10))
    pass