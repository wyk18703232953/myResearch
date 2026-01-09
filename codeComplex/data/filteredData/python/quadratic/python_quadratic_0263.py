def main(n):
    # Deterministically generate a, b from n
    # Ensure a, b are positive and vary with n
    a = n % 5 + 1
    b = (n // 3) % 5 + 1

    # Core logic from original code
    if min(a, b) > 1 or (1 < n < 4 and max(a, b) == 1):
        # print('NO')
        pass
        return
    # print('YES')
    pass
    f = int(a == 1)
    g = [a, b][f]
    r = [[f] * n for _ in range(n)]
    for i in range(n):
        r[i][i] = 0
    for i in range(n - g):
        r[i][i + 1] ^= 1
        r[i + 1][i] ^= 1
    for x in r:
        # print(*x, sep='')
        pass
if __name__ == "__main__":
    main(5)