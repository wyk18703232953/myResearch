def main(n):
    # n controls both list sizes and the value m
    if n <= 0:
        return
    m = n

    # Deterministically generate arrays a and b of length n
    # a: pattern with a clear max, repeated in a controlled way
    # b: pattern with a clear min, related to a but not random
    a = [(i * 2 + 3) % (n + 5) + 1 for i in range(n)]
    b = [((i * 3 + 1) % (n + 7)) + 1 for i in range(n)]

    ma = 0
    macount = 0
    mi = 1000000000000000000000000000
    su = 0

    for el in a:
        if el > ma:
            ma = el
            macount = 1
        elif el == ma:
            macount += 1

    for el in b:
        if el < mi:
            mi = el
        su += el

    if ma > mi:
        # print(-1)
        pass
    elif ma == mi or macount > 1:
        f = True
        for i in range(n):
            if a[i] == ma and f:
                f = False

            else:
                su += a[i] * m
        # print(su)
        pass

    else:
        secmax = 0
        for el in a:
            if secmax < el < ma:
                secmax = el
        f = True
        for i in range(n):
            if a[i] == ma and f:
                f = False

            else:
                su += a[i] * m
        # print(su + ma - secmax)
        pass
if __name__ == "__main__":
    main(10)