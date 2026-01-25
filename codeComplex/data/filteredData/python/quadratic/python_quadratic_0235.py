def main(n):
    # Ensure n is at least 3 to allow meaningful triples; smaller n will behave but are trivial
    if n <= 0:
        print(-1)
        return

    # Deterministic generation of s and a based on n
    # s: increasing-ish sequence with some variation
    s = [i * 2 + (i % 3) for i in range(n)]
    # a: positive costs with small variation but bounded and deterministic
    a = [(i % 7) + 1 for i in range(n)]

    t = 3 * 10**9
    q = [0] * n
    for i in range(n - 1, -1, -1):
        u = 10**8
        for j in range(i - 1, -1, -1):
            if s[i] > s[j]:
                if a[j] < u:
                    u = a[j]
        q[i] = u

    for i in range(n):
        for j in range(i + 1, n):
            if s[i] < s[j]:
                cand = a[i] + a[j] + q[i]
                if cand < t:
                    t = cand

    total_a = sum(a)
    print(t if t <= total_a else -1)


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)