def main(n):
    # Interpret n as both dimensions for determinism: original code expects n, m
    # Here we set m = n so input scale is controlled by a single parameter
    m = n

    np1 = n + 1
    mp1 = m + 1

    for i in range(1, 1 + n // 2):
        for j in range(1, mp1):
            # print('%d %d\n%d %d' % (i, j, np1 - i, mp1 - j))
            pass
    if n & 1:
        i = 1 + n // 2
        for j in range(1, 1 + m // 2):
            # print('%d %d\n%d %d' % (i, j, i, mp1 - j))
            pass
        if m & 1:
            # print(i, 1 + m // 2)
            pass
if __name__ == "__main__":
    main(5)