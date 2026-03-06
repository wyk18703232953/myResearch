import sys

INF = 10**9

def solve(n, m, s):
    count = [[0] * m for _ in range(m)]
    ord_a = ord("a")
    for c1, c2 in zip(s, s[1:]):
        c1 = ord(c1) - ord_a
        c2 = ord(c2) - ord_a
        if c1 != c2:
            count[c1][c2] += 1

    sum_of_subset = [[0] * (1 << m) for _ in range(m)]
    for i in range(m):
        for j in range(1 << m):
            if j == 0:
                continue
            lsb = j & -j
            sum_of_subset[i][j] = sum_of_subset[i][j ^ lsb] + count[i][lsb.bit_length() - 1]

    adj_in_subset = [0] * (1 << m)
    for i in range(1 << m):
        for j in range(m):
            if i & (1 << j):
                adj_in_subset[i] += sum_of_subset[j][i]

    total_adj = adj_in_subset[-1]
    dp = [INF] * (1 << m)
    dp[0] = 0

    for i in range(1 << m):
        for j in range(m):
            if i & (1 << j):
                continue
            not_i = ((1 << m) - 1) ^ i
            val = dp[i] + (total_adj - adj_in_subset[i] - adj_in_subset[not_i])
            nxt = i | (1 << j)
            if val < dp[nxt]:
                dp[nxt] = val
    return dp[-1]


def main(n):
    # n controls both string length and alphabet size deterministically
    # Keep m reasonably bounded by bits in n to avoid 2^m blowup
    m = max(1, min(10, (n.bit_length() % 10) + 1))
    if n < 2:
        n_eff = 2
    else:
        n_eff = n

    # Generate a deterministic string of length n_eff over m characters 'a'..'a'+m-1
    chars = [chr(ord('a') + (i % m)) for i in range(n_eff)]
    s = ''.join(chars)

    res = solve(n_eff, m, s)
    print(res)


if __name__ == "__main__":
    # Example deterministic call; change the constant to scale input size
    main(1000)