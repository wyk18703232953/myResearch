def main(n):
    # Interpret n as the size of the array and let m = n
    m = n

    # Deterministically generate array a of length m with values in [1, max(1, n//3)]
    if n == 0:
        # print(0)
        pass
        return
    value_range = max(1, n // 3)
    a = [(i % value_range) + 1 for i in range(m)]

    d = {i: 0 for i in set(a)}
    for i in range(m):
        d[a[i]] += 1
    k = 1
    while sum(d[i] // k for i in d) >= n:
        k += 1
    # print(k - 1)
    pass
if __name__ == "__main__":
    main(10)