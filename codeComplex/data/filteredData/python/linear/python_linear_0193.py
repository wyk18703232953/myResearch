def main(n):
    # Deterministically generate parameters based on n
    # Ensure t is at least 2 to make range(1, t) non-empty and indices valid
    a = n % 7 + 1
    b = n % 5 + 1
    c = n % 6 + 1
    t = max(2, n + 1)

    # Generate list l of size n with values in [1, min(1000, t-1)]
    max_val = min(1000, t - 1)
    if max_val <= 0:
        max_val = 1
    l = [(i % max_val) + 1 for i in range(n)]

    f = [0] * 1001
    for i in l:
        if 0 <= i <= 1000:
            f[i] += 1

    tmp = 0
    for i in range(1, t):
        if i <= 1000:
            tmp += (t - i) * f[i]

    tmp = n * a + tmp * c - tmp * b
    result = max(n * a, tmp)
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(10)