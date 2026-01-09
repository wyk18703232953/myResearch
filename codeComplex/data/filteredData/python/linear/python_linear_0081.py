def main(n):
    # Generate deterministic binary strings a and b based on n
    # Let len(a) = n, len(b) = 2n (so m >= n and scalable)
    a = [(i % 2) for i in range(n)]
    m = 2 * n
    b = [((i // 2) % 2) for i in range(m)]

    ans = 0
    for i in range(n):
        ans += a[i] ^ b[i]

    ones = [0 for _ in range(m)]
    zeros = [0 for _ in range(m)]

    for i in range(m):
        if b[i]:
            ones[i] = 1

        else:
            zeros[i] = 1

    for i in range(1, m):
        ones[i] += ones[i - 1]
        zeros[i] += zeros[i - 1]

    for i in range(n):
        if a[i] == 1:
            ans += zeros[m - n + i] - zeros[i]

        else:
            ans += ones[m - n + i] - ones[i]

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)