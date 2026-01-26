def main(n):
    # Interpret n as the number of elements
    # Generate deterministic parameters and array
    l = n
    r = 3 * n
    d = max(1, n // 3)
    p = [i + 1 for i in range(n)]

    t = 0
    for v in range(1, 2 ** n):
        s = []
        for i in range(n):
            if v & (1 << i):
                s.append(p[i])
        if s:
            s_sum = sum(s)
            if l <= s_sum <= r and max(s) - min(s) >= d:
                t += 1
    print(t)


if __name__ == "__main__":
    main(10)