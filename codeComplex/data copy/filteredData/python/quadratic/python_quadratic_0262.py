def main(n):
    a = 1 + (n % 3)
    b = 1 + ((2 * n) % 3)
    z, o = ('01', '10')[a < b]
    n_adj = n
    n_adj *= not (a > 1 < b or 1 < n_adj * a * b < 4)
    l = [[z] * n_adj for _ in range(n_adj)]
    for i in range(n_adj):
        l[i][i] = '0'
    for i in range(n_adj - a * b):
        l[i][i + 1] = l[i + 1][i] = o
    # print(('YES', 'NO')[not n_adj])
    pass
    # print('\n'.join(map(''.join, l)))
    pass
if __name__ == "__main__":
    main(5)