def main(n):
    # 生成确定性输入：n, a, b
    # 为了覆盖不同情况，这里把 a, b 设成 n 的简单函数
    # 保证 a, b >= 1
    a = max(1, n % 5)
    b = max(1, (n // 2) % 5)
    # 避免 a * b > n 导致循环为负，简单裁剪一下
    if a * b > n and a > 1:
        a = 1
    if a * b > n and b > 1:
        b = 1

    if a > 1 < b or a * b == 1 and 1 < n < 4:
        print('NO')
    else:
        z, o = ('01', '10')[a < b]
        l = [[z] * n for _ in range(n)]
        for i in range(n):
            l[i][i] = '0'
        for i in range(n - a * b):
            l[i][i + 1] = l[i + 1][i] = o
        print('YES')
        print('\n'.join(map(''.join, l)))


if __name__ == "__main__":
    main(6)