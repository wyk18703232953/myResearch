import sys

def build_input(n):
    # n is the width of each of the 4 rows
    if n <= 0:
        n = 1
    cost = [0, 3, 5, 7, 11]
    # Build 4 deterministic rows, length n each
    a = []
    for y in range(4):
        row_chars = []
        for x in range(n):
            val = (y * 17 + x * 23) % 5
            if val == 0:
                row_chars.append('.')

            else:
                row_chars.append('#')
        a.append(''.join(row_chars))
    return n, cost, a

def main(n):
    n, cost, a = build_input(n)

    mask = [0, 1, 51, 1911]
    inf, bs_size, full_bit = 10**9, 1 << 12, (1 << 12) - 1
    dp = [[inf] * bs_size for _ in range(4 * n + 1)]
    dp[0][0] = 0

    for i in range(4 * n):
        y, x = i & 3, i >> 2
        is_dot = 1 if a[y][x] == '.' else 0

        for bitset in range(bs_size):
            if dp[i][bitset] == inf:
                continue

            if y == 0:
                if dp[i + 4][full_bit] > dp[i][bitset] + cost[4]:
                    dp[i + 4][full_bit] = dp[i][bitset] + cost[4]

            if (is_dot | (bitset & 1)) and dp[i + 1][bitset >> 1] > dp[i][bitset]:
                dp[i + 1][bitset >> 1] = dp[i][bitset]

            for k in range(1, min(4 - y, 3) + 1):
                new_mask = bitset | mask[k]
                if dp[i][new_mask] > dp[i][bitset] + cost[k]:
                    dp[i][new_mask] = dp[i][bitset] + cost[k]

    result = min(dp[4 * n])
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(10)