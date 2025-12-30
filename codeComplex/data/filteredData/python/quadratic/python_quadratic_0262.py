def main(n: int) -> None:
    # 根据 n 生成一组 a, b，使得逻辑有一定代表性
    # 这里简单选择：a = 2, b = max(1, n // 2)
    # 可按需要修改生成策略
    a = 2
    b = max(1, n // 2)

    z, o = ('01', '10')[a < b]
    valid_n = n
    valid_n *= not (a > 1 < b or 1 < n * a * b < 4)

    l = [[z] * valid_n for _ in range(valid_n)]
    for i in range(valid_n):
        l[i][i] = '0'
    for i in range(valid_n - a * b):
        l[i][i + 1] = l[i + 1][i] = o

    print(('YES', 'NO')[not valid_n])
    print('\n'.join(map(''.join, l)))


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)