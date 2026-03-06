import sys
sys.setrecursionlimit(10**7)

INF = 10**9

def solve(n, m, s):
    adj_in_subset = [0] * (1 << m)
    ord_a = ord("a")
    for c1, c2 in zip(s, s[1:]):
        c1 = ord(c1) - ord_a
        c2 = ord(c2) - ord_a
        if c1 != c2:
            adj_in_subset[(1 << c1) + (1 << c2)] += 1
    for i in range(m):
        for j in range(1 << m):
            if j & (1 << i):
                adj_in_subset[j] += adj_in_subset[j ^ (1 << i)]

    total_adj = adj_in_subset[-1]
    dp = [INF] * (1 << m)
    dp[0] = 0

    full_mask = (1 << m) - 1
    for i in range(1 << m):
        for j in range(m):
            if i & (1 << j):
                continue
            comp_mask = full_mask ^ i
            cost = total_adj - adj_in_subset[i] - adj_in_subset[comp_mask]
            nxt = i | (1 << j)
            if dp[nxt] > dp[i] + cost:
                dp[nxt] = dp[i] + cost
    return dp[-1]

def generate_input(n):
    # Map n to m (alphabet size) and length of string
    # Ensure m is not too large for 2^m complexity
    if n <= 0:
        m = 1
    else:
        m = (n % 10) + 1  # m in [1,10]
    length = max(2, n)

    # Deterministic string generation using simple arithmetic
    # Characters cycle over first m letters
    s_chars = []
    for i in range(length):
        c = chr(ord('a') + (i * 3 + 1) % m)
        s_chars.append(c)
    s = "".join(s_chars)
    return length, m, s

def main(n):
    n_val, m, s = generate_input(n)
    result = solve(n_val, m, s)
    print(result)

if __name__ == "__main__":
    main(5)