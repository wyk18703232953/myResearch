def main(n):
    # Ensure n is at least 1
    if n < 1:
        n = 1

    # Define sizes for a and b based on n
    len_a = n
    len_b = 2 * n

    # Deterministic generation of a and b as lists of 0/1 integers
    # Pattern: a[i] = i % 2, b[i] = (i // 2) % 2
    a = [i % 2 for i in range(len_a)]
    b = [(i // 2) % 2 for i in range(len_b)]

    n_len = len_a
    m_len = len_b

    ans = 0
    for i in range(n_len):
        ans += a[i] ^ b[i]

    ones = [0 for _ in range(m_len)]
    zeros = [0 for _ in range(m_len)]

    for i in range(m_len):
        if b[i]:
            ones[i] = 1
        else:
            zeros[i] = 1

    for i in range(1, m_len):
        ones[i] += ones[i - 1]
        zeros[i] += zeros[i - 1]

    for i in range(n_len):
        if a[i] == 1:
            ans += zeros[m_len - n_len + i] - zeros[i]
        else:
            ans += ones[m_len - n_len + i] - ones[i]

    print(ans)


if __name__ == "__main__":
    # Example call; change n to scale input size
    main(5)