def main(n):
    # Deterministically generate a, b based on n
    # Ensure a and b are at least 1
    a = (n % 3) + 1
    b = ((n // 2) % 3) + 1

    c = max(a, b)
    if a != 1 and b != 1:
        # print('NO')
        pass
        return
    if n == 2 and c == 1:
        # print('NO')
        pass
        return
    if n == 3 and c == 1:
        # print('NO')
        pass
        return

    if a == 1:
        g = [[1] * n for _ in range(n)]
        for i in range(n):
            g[i][i] = 0
        for i in range(c - 1, n - 1):
            g[i][i + 1] = g[i + 1][i] = 0

    else:
        g = [[0] * n for _ in range(n)]
        for i in range(c - 1, n - 1):
            g[i][i + 1] = g[i + 1][i] = 1

    # print('YES')
    pass
    for r in g:
        # print(''.join(str(x) for x in r))
        pass
if __name__ == "__main__":
    # Example call for complexity experiments
    main(10)