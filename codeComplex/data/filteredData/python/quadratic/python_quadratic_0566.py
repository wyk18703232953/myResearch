def main(n: int) -> None:
    # 根据 n 生成测试数据，这里令 m = n（也可以按需修改为其他规则）
    m = n

    buf = []
    for i in range(n // 2):
        for j in range(m):
            buf.append(f'{i + 1} {j + 1}\n')
            buf.append(f'{n - i} {m - j}\n')

    if n % 2 == 1:
        for j in range(m // 2):
            buf.append(f'{n // 2 + 1} {j + 1}\n')
            buf.append(f'{n // 2 + 1} {m - j}\n')
        if m % 2 == 1:
            buf.append(f'{n // 2 + 1} {m // 2 + 1}\n')

    # print(*buf, sep='')
    pass
if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)