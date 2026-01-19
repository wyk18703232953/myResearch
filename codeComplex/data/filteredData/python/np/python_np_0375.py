def main(n):
    # Interpret n as the length of the string a, with fixed m=20 to match bit-size in original code
    m = 20
    if n < 2:
        # For very small n, construct a minimal non-empty string
        n = 2

    # Deterministic construction of a string a of length n over first m letters
    # a[i] cycles through 'a'..'t' (20 letters)
    a = [chr(ord('a') + (i % m)) for i in range(n)]

    dp = [10 ** 10] * (1 << m)
    cnt = [0] * (1 << m)

    def get(x):
        return 1 << (ord(x) - ord('a'))

    for i in range(1, n):
        cnt[get(a[i]) | get(a[i - 1])] += 1

    for i in range(m):
        for j in range(1 << m):
            if (1 << i) & j:
                cnt[j] += cnt[j ^ (1 << i)]

    dp[0] = 0

    full_mask = (1 << m) - 1
    for i in range(1 << m):
        for j in range(m):
            if not (i & (1 << j)):
                nxt = i | (1 << j)
                dp[nxt] = min(
                    dp[nxt],
                    dp[i] + n - 1 - cnt[nxt] - cnt[full_mask - nxt],
                )

    return dp[full_mask]


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    result = main(100)
    print(result)