def main(n):
    # Interpret n as the size of the array l; keep m and k fixed relative to n.
    # To preserve the original behavior where m is a separate parameter, we
    # choose a deterministic mapping from n:
    # - m is at least 1 and at most n
    # - k scales with n so that subtraction has visible effect
    if n <= 0:
        return

    # Deterministic parameter generation based on n
    m = max(1, n // 3)  # window size, at least 1
    k = n // 2          # cost parameter

    # Deterministic test data l of length n
    # Use a simple arithmetic pattern so behavior is stable and scalable
    l = [(i * 2 - 3 * (i % 4)) for i in range(n)]

    ma = 0
    # Guard for m possibly larger than n due to mapping changes
    m_eff = min(m, n)

    # Original logic: deb from n-1 down to n-m
    for deb in range(n - 1, n - m_eff - 1, -1):
        cumi = 0
        scu = 0
        for i in range(deb, -1, -1):
            scu += l[i]
            ma = max(ma, scu - cumi - k)
            if (deb - i + 1) % m_eff == 0:
                scu -= k
            if scu < cumi:
                cumi = scu

    print(ma)


if __name__ == "__main__":
    # Example deterministic call; change n to scale input size
    main(10)