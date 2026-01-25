def main(n):
    # Interpret n as the size of the matrix; deterministically derive a and b from n
    if n < 2:
        # For n < 2, the original logic is not meaningful; just do nothing
        return

    # Deterministic generation of a, b based on n
    # Ensure a, b are at least 1
    a = (n % 3) + 1
    b = (n % 5) + 1

    c = max(a, b)
    if a != 1 and b != 1:
        print('NO')
    elif n == 2 and c == 1:
        print('NO')
    elif n == 3 and c == 1:
        print('NO')
    else:
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
        print('YES')
        for r in g:
            print(''.join(str(x) for x in r))


if __name__ == "__main__":
    main(5)