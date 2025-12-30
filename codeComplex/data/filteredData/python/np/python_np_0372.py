import sys
sys.setrecursionlimit(10**7)

INF = 10**9


def main(n: int):
    """
    n: problem size, here used as length of string s.
       Alphabet size m is fixed to 20 as in the original program.
    """
    # You can change how test data is generated here.
    # We keep m fixed to make the bitmask DP meaningful.
    m = 20
    ord_a = ord("a")

    # Generate test string s of length n over first m letters.
    # Simple deterministic pattern: repeating 'a'..('a'+m-1)
    chars = [chr(ord_a + (i % m)) for i in range(n)]
    s = "".join(chars)

    # Original logic starts here
    count = [[0] * m for _ in range(m)]

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
        ssum = 0
        for j in range(m):
            if i & (1 << j):
                ssum += sum_of_subset[j][i]
        adj_in_subset[i] = ssum

    total_adj = adj_in_subset[-1]
    dp = [INF] * (1 << m)
    dp[0] = 0

    full_mask = (1 << m) - 1
    for i in range(1 << m):
        cur = dp[i]
        if cur == INF:
            continue
        not_i = full_mask ^ i
        base = cur + (total_adj - adj_in_subset[i] - adj_in_subset[not_i])
        # try placing each character j not in i
        rem = not_i
        while rem:
            lsb = rem & -rem
            j = lsb.bit_length() - 1
            nxt = i | (1 << j)
            if base < dp[nxt]:
                dp[nxt] = base
            rem ^= lsb

    # For library-like usage we return the answer instead of printing
    return dp[-1]


if __name__ == "__main__":
    # example call; you can change n for testing
    ans = main(5)
    print(ans)