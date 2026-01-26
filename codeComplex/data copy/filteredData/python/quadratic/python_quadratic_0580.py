def main(n):
    # We interpret n as the length of the string s.
    # We fix a single test case and choose k deterministically from n.
    # Ensure k is at least 1 and at most n.
    if n <= 0:
        return
    if n == 1:
        k = 1

    else:
        k = max(1, min(n, n // 2))

    # Deterministically generate s of length n using pattern over 'R', 'G', 'B'
    base = "RGB"
    s = "".join(base[i % 3] for i in range(n))

    # Core logic from original program, adapted for a single test case without input()
    p = (k + 2) // 2
    l = "RGB" * p
    res = n
    for i in range(n - k + 1):
        c = 0
        for j in range(0, k):
            c += (s[i + j] != l[j])
        res = min(res, c)

        c = 0
        for j in range(1, k + 1):
            c += (s[i + j - 1] != l[j])
        res = min(res, c)

        c = 0
        for j in range(2, k + 2):
            c += (s[i + j - 2] != l[j])
        res = min(res, c)

    # print(res)
    pass
if __name__ == "__main__":
    # Example deterministic call for experimentation
    main(100)