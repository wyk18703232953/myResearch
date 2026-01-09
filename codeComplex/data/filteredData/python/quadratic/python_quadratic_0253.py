def main(n):
    # Deterministic generation of a, b based on n
    a = n % 5 + 1
    b = (n // 3) % 5 + 1

    if a > 1 < b or a * b == 1 and 1 < n < 4:
        # print('NO')
        pass

    else:
        z, o = ('01', '10')[a < b]
        l = [[z] * n for _ in range(n)]
        for i in range(n):
            l[i][i] = '0'
        for i in range(max(0, n - a * b)):
            if i + 1 < n:
                l[i][i + 1] = o
                l[i + 1][i] = o
        # print('YES')
        pass
        # print('\n'.join(''.join(row) for row in l))
        pass
if __name__ == "__main__":
    main(5)