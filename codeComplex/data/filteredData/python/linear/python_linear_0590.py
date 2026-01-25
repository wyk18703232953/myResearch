import math

def main(n):
    # Ensure n is at least 1
    if n <= 0:
        return

    # Deterministic generation of input data based on n
    # String length = n
    # q (number of queries) = n
    # s is a binary string of length n, deterministically generated
    q = n
    s = [(i * 7 + 3) % 2 for i in range(n)]

    prefix = [0] * n
    prefix[0] = s[0]
    temp = [0] * (n + 1)
    temp[0] = 1
    mod = (pow(10, 9) // 1) + 7

    for i in range(1, n):
        prefix[i] = prefix[i - 1] + s[i]
        temp[i] = (2 * (temp[i - 1] % mod)) % mod

    temp[n] = (2 * (temp[n - 1] % mod)) % mod

    # Deterministic queries: q intervals [l, r]
    # Use simple modular arithmetic to spread intervals across [0, n-1]
    queries = []
    for i in range(q):
        l = (i * 3) % n
        r = (l + (i * 5 + 1) % n)
        if r >= n:
            r = n - 1
        if l > r:
            l, r = r, l
        queries.append((l, r))

    ansarr = []
    for l, r in queries:
        a = prefix[r] - prefix[l] + s[l]
        d = r - l + 1
        val1 = temp[d]
        val2 = temp[d - a]
        ansarr.append((val1 - val2) % mod)

    print("\n".join(map(str, ansarr)))


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)