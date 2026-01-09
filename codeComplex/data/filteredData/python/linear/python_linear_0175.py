def main(n):
    # Define k as a window size based on n
    if n <= 0:
        return
    k = max(1, n // 3)

    # Deterministically generate arrays a and t of length n
    # a: positive integers with simple pattern
    a = [(i * 7) % 100 + 1 for i in range(n)]
    # t: 0/1 pattern based on i
    t = [1 if (i % 3 == 0) else 0 for i in range(n)]

    x = 0
    summ = 0
    maxx = 0

    for i in range(n):
        summ += a[i] * t[i]

    for i in range(k):
        if not t[i]:
            x += a[i]
    maxx = max(maxx, x)

    for i in range(n - k):
        x += a[i + k] * (1 - t[i + k])
        x -= a[i] * (1 - t[i])
        if x > maxx:
            maxx = x

    # print(summ + maxx)
    pass
if __name__ == "__main__":
    main(10)