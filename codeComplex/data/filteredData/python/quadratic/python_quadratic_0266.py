def main(n):
    # deterministically generate a, b from n
    if n < 1:
        return
    a = max(1, (n % 3) + 1)
    b = 1 if a != 1 else 2

    if min(a, b) > 1:
        print('NO')
        return

    M = [[0] * n for _ in range(n)]

    if a == 1 and b == 1:
        if n == 1:
            print('YES')
            print('0')
            return
        if n == 2 or n == 3:
            print('NO')
            return
        for i in range(1, n):
            M[i - 1][i] = 1
            M[i][i - 1] = 1
    else:
        s = n - max(a, b) + 1
        for i in range(s):
            for j in range(s):
                if i != j:
                    M[i][j] = 1
        if a == 1:
            for i in range(n):
                for j in range(n):
                    if i != j:
                        M[i][j] = 1 - M[i][j]

    print('YES')
    for i in range(n):
        print(''.join(map(str, M[i])))


if __name__ == "__main__":
    main(5)