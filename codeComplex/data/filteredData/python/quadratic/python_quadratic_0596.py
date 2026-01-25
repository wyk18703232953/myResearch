def main(n):
    # Interpret n as the input size (length of array a)
    if n <= 0:
        return 0

    # Deterministically choose m and k based on n
    # Ensure 1 <= m <= n
    m = max(1, n // 3)
    k = max(1, n // 5)

    # Deterministically generate array a of length n
    # Example pattern: a[i] = (i % 7) - 3
    a = [(i % 7) - 3 for i in range(n)]

    def f(o):
        r = 0
        e = 0
        for i, x in enumerate(a):
            if i < o:
                continue
            if i % m == o:
                e -= k
                if e < -k:
                    e = -k
            e += x
            if e > r:
                r = e
        return r

    result = max(f(o) for o in range(m))
    print(result)
    return result


if __name__ == "__main__":
    # Example deterministic call for experimentation
    main(1000)