def main(n):
    if n <= 0:
        print("YES")
        print()
        return

    # Deterministic construction of l and r based on n
    # l[i] = number of j < i with j > i  -> always 0
    # r[i] = number of j > i with j > i  -> n-1 - i
    l = [0] * n
    r = [n - 1 - i for i in range(n)]

    c = [n] * n
    for i in range(n):
        c[i] -= (r[i] + l[i])

    for i in range(n):
        m = 0
        for j in range(0, i):
            if c[j] > c[i]:
                m += 1
        if m != l[i]:
            print('NO')
            return

    for i in range(n):
        m = 0
        for j in range(i + 1, n):
            if c[j] > c[i]:
                m += 1
        if m != r[i]:
            print('NO')
            return

    print('YES')
    print(*c)


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(5)