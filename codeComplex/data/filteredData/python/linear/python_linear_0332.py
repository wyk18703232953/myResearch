def main(n):
    # Interpret n as the number of segments where the light may toggle.
    # Generate deterministic M and a[] based on n.
    # Original input format:
    # n M
    # a1 a2 ... an
    #
    # Here:
    #   M = 2 * n + 3 (ensures M > last a[i])
    #   a[i] = 2 * i - 1, strictly increasing in [1, 2n-1]
    #
    # This preserves basic spacing and parity structure for complexity experiments.
    M = 2 * n + 3
    a = [0] + [2 * i - 1 for i in range(1, n + 1)] + [M]

    ontime = [0] * (n + 1)
    tmp = 0
    for ind in range(n, -1, -1):
        if ind % 2 == 0:
            tmp += a[ind + 1] - a[ind]
        ontime[ind] = tmp

    mx = ontime[0]
    for ind in range(n + 1):
        l, r = a[ind], a[ind + 1]
        if r - l <= 1:
            continue
        for x in (l + 1, r - 1):
            newtime = ontime[0] - ontime[ind]
            if ind % 2 == 0:
                newtime += x - l

            else:
                newtime += r - x
            newtime += (M - r) - ontime[ind]
            if newtime > mx:
                mx = newtime

    # print(mx)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n to scale input size
    main(5)