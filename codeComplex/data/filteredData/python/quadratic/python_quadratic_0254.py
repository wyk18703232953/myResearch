def main(n):
    a = 2 + (n % 3)
    b = 2 + (n % 5)
    z, o = ('01', '10')[a < b]
    n_flag = n
    n_flag *= not (a > 1 < b or 1 < n_flag * a * b < 4)
    l = [[z] * n_flag for _ in range(n_flag)]
    for i in range(n_flag):
        l[i][i] = '0'
    for i in range(n_flag - a * b):
        l[i][i + 1] = l[i + 1][i] = o
    print(('YES', 'NO')[not n_flag])
    if n_flag:
        print('\n'.join(map(''.join, l)))


if __name__ == "__main__":
    main(10)