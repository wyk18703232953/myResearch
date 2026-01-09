def main(n):
    # 根据 n 生成测试数据：a, b
    # 这里给一个简单策略，你可按需要修改：
    # - 当 n 较大时，给一些不同组合保证覆盖原逻辑分支
    if n <= 0:
        # 原代码中如果 n 为 0，后续会打印 NO 并且矩阵为空
        # 为保持结构，这里还是生成 a, b，但不会真正用到矩阵
        a, b = 1, 1

    else:
        # 示例：让 a, b 随 n 变化，覆盖不同情况
        if n == 1:
            a, b = 1, 1
        elif n == 2:
            a, b = 1, 2
        elif n == 3:
            a, b = 2, 1

        else:
            # n >= 4 时给一个稳定可行的数据
            a, b = 2, 2

    # 以下为原逻辑的无 input 封装
    z, o = ('01', '10')[a < b]
    n = int(n)  # 确保是整数
    n *= not (a > 1 < b or 1 < n * a * b < 4)

    l = [[z] * n for _ in range(n)]
    for i in range(n):
        l[i][i] = '0'
    for i in range(n - a * b):
        l[i][i + 1] = l[i + 1][i] = o

    # print(('YES', 'NO')[not n])
    pass
    # print('\n'.join(map(''.join, l)))
    pass
if __name__ == "__main__":
    # 示例运行：可按需修改 n
    main(4)