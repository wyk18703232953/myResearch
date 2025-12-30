import sys

def main(n):
    # 根据 n 生成测试数据，这里设定 m 与 n 相同作为规模示例
    m = n

    # 原逻辑：输出成对坐标
    for i in range(1, n // 2 + 1):
        for j in range(1, m + 1):
            sys.stdout.write("".join((str(i), " ", str(j), "\n")))
            sys.stdout.write("".join((str(n - i + 1), " ", str(m - j + 1), "\n")))

    if n % 2 == 1:
        for j in range(1, m // 2 + 1):
            sys.stdout.write("".join((str(n // 2 + 1), " ", str(j), "\n")))
            sys.stdout.write("".join((str(n // 2 + 1), " ", str(m - j + 1), "\n")))

        if m % 2 == 1:
            sys.stdout.write("".join((str(n // 2 + 1), " ", str(m // 2 + 1), "\n")))


if __name__ == "__main__":
    # 示例：调用 main(5)，实际使用时可根据需要修改 n
    main(5)