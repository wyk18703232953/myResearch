def main(n):
    # Interpret n as the length of arrays a and b, m is fixed as n for scalability
    m = n
    if n <= 0:
        return

    # Deterministically generate arrays a and b based on n
    # a: mix of increasing and modular pattern
    a = [(i * 3 + 1) % (n + 5) for i in range(n)]
    # b: shifted pattern to vary minimum relative to a's maximum
    b = [(i * 2 + 7) % (n + 11) for i in range(n)]

    ma = 0
    macount = 0
    mi = 10**30
    su = 0

    # Process a
    for el in a:
        if el > ma:
            ma = el
            macount = 1
        elif el == ma:
            macount += 1

    # Process b
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