def main(n):
    # 映射规则：
    # 对于给定的 n，构造一个 n x n 的网格，即 n 行 n 列
    rows = n
    cols = n

    buf = []
    for i in range(rows // 2):
        for j in range(cols):
            buf.append(f'{i + 1} {j + 1}\n')
            buf.append(f'{rows - i} {cols - j}\n')

    if rows % 2 == 1:
        for j in range(cols // 2):
            buf.append(f'{rows // 2 + 1} {j + 1}\n')
            buf.append(f'{rows // 2 + 1} {cols - j}\n')
        if cols % 2 == 1:
            buf.append(f'{rows // 2 + 1} {cols // 2 + 1}\n')

    print(*buf, sep='')


if __name__ == "__main__":
    # 示例：以 n = 5 运行主函数，可根据需要修改 n 的数值
    main(5)