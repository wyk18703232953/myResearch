def main(n):
    # Deterministic generation of a, b from n
    # Ensure a, b >= 1 and <= n
    a = n % max(1, n) + 1 if n > 1 else 1
    b = (n // 2) % max(1, n) + 1 if n > 1 else 1
    if a > n:
        a = n
    if b > n:
        b = n

    a0 = a
    b0 = b
    if a0 > b0:
        a0, b0 = b, a

    if n == 2 and (a0, b0) == (1, 1):
        # print('NO')
        pass
        return
    if n == 3 and (a0, b0) == (1, 1):
        # print('NO')
        pass
        return
    if a > 1 and b > 1:
        # print('NO')
        pass
        return

    mat = [['0' for _ in range(n)] for _ in range(n)]
    mat1 = [['1' for _ in range(n)] for _ in range(n)]
    if b == 1:
        for x in range(n - a):
            mat[x][x + 1] = '1'
            mat[x + 1][x] = '1'

    else:
        mat = mat1
        for x in range(n):
            mat[x][x] = '0'
        for x in range(n - b):
            mat[x][x + 1] = '0'
            mat[x + 1][x] = '0'

    # print('YES')
    pass
    for x in range(n):
        # print(''.join(mat[x]))
        pass
if __name__ == "__main__":
    main(5)