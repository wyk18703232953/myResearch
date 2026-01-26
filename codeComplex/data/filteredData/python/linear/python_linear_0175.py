def main(n):
    # n controls both array length and window size k
    if n <= 0:
        return 0

    # define length and k deterministically
    length = n
    k = max(1, min(n, n // 2))

    # deterministic construction of a and t
    a = [i % 7 + 1 for i in range(length)]
    t = [1 if i % 3 == 0 else 0 for i in range(length)]

    # original logic
    x = 0
    summ = 0
    maxx = 0

    for i in range(length):
        summ += a[i] * t[i]

    for i in range(k):
        if not t[i]:
            x += a[i]
    maxx = max(maxx, x)

    for i in range(length - k):
        x += a[i + k] * (1 - t[i + k])
        x -= a[i] * (1 - t[i])
        if x > maxx:
            maxx = x

    result = summ + maxx
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # example deterministic call
    main(10)