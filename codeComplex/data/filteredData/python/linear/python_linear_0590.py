def main(n):
    # Interpret n as both the string length and the number of queries
    # Generate a deterministic binary string of length n
    # s[i] = i % 2  -> pattern "0101..."
    s = [i % 2 for i in range(n)]
    q = n

    prefix = [0] * n
    prefix[0] = s[0]
    temp = [0] * (n + 1)
    temp[0] = 1
    mod = (10**9) + 7

    for i in range(1, n):
        prefix[i] = prefix[i - 1] + s[i]
        temp[i] = (2 * temp[i - 1]) % mod

    temp[n] = (2 * temp[n - 1]) % mod

    # Generate q deterministic queries (l, r), 1-based in original code
    # Here we create intervals with varying lengths covering the array.
    queries = []
    for i in range(q):
        if n == 0:
            break
        l = (i * 2) % max(1, n)           # 0-based
        r = min(n - 1, l + (i % max(1, n)))  # ensure r >= l and within bounds
        # convert to 1-based style as original code expects, then subtract 1 back
        queries.append((l + 1, r + 1))

    ansarr = []
    for l1, r1 in queries:
        l = l1 - 1
        r = r1 - 1
        a = prefix[r] - prefix[l] + s[l]
        d = r - l + 1
        val1 = temp[d]
        val2 = temp[d - a]
        ansarr.append((val1 - val2) % mod)

    # For experiment usage, just print the answers
    if ansarr:
        # print("\n".join(map(str, ansarr)))
        pass

    else:
        # print()
        pass
if __name__ == "__main__":
    # Example call for time-complexity experiments
    main(10)