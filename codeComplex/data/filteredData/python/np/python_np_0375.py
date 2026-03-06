def main(n):
    # Map n to string length, fix m=5 for scalability while keeping complexity meaningful
    m = 5
    if n < 2:
        n = 2

    # Deterministically generate a string of length n over first m letters
    # pattern: a,b,c,d,e,a,b,c,d,e,...
    letters = [chr(ord('a') + (i % m)) for i in range(n)]
    a = letters

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

    full = (1 << m) - 1
    for i in range(1 << m):
        for j in range(m):
            if not i & (1 << j):
                nxt = i | (1 << j)
                dp[nxt] = min(
                    dp[nxt],
                    dp[i] + n - 1 - cnt[nxt] - cnt[full - nxt]
                )

    return dp[full]


if __name__ == "__main__":
    # example call
    print(main(10))