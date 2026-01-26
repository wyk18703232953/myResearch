def main(n):
    # Interpret n as array length; generate m = max value bound deterministically
    if n <= 0:
        # print(0)
        pass
        return

    m = max(1, n // 2)
    # Deterministic construction of array a of length n with values depending on n and index
    a = [(i % m) + 1 for i in range(n)]

    # Core algorithm logic preserved
    a.sort()
    last = 0
    total = 0
    for i in range(n - 1):
        if a[i] > 0:
            total += a[i] - 1
            last = min(last + 1, a[i])

    result = total + max(a[n - 1] - max(1, a[n - 1] - last), 0)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)