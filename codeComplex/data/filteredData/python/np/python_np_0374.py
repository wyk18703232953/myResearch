import sys

INF = 10**9

def main(n):
    # Derive m (alphabet size) from n in a deterministic, scalable way
    # Keep m reasonably small so 2^m is computable; use m up to 18
    if n <= 0:
        m = 1
    else:
        m = max(1, min(18, n // 100 if n >= 100 else n // 10 + 1))

    # Define string length as linear in n, at least m+1 so adjacency exists
    length = max(m + 1, n if n > 0 else m + 1)

    # Deterministically generate string s of length "length" over first m letters
    chars = []
    for i in range(length):
        c = (i * 17 + i // 3) % m
        chars.append(chr(ord("a") + c))
    s = "".join(chars)

    # Original core algorithm starts here
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
            # Use full_mask instead of ~i to keep indices within range
            cost = total_adj - adj_in_subset[i] - adj_in_subset[full_mask ^ i]
            nxt = i | (1 << j)
            cand = dp[i] + cost
            if cand < dp[nxt]:
                dp[nxt] = cand

    result = dp[-1]
    print(result)
    return result

if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(1000)