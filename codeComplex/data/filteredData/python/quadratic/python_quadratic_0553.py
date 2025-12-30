def main(n):
    # 生成测试数据：原程序从输入读入 x, y，这里统一设为 n, n
    x, y = n, n

    a = 0
    b = x * y
    pos = True

    for t in reversed(range(b)):
        b -= 1
        print(str(int(a / y + 1)) + ' ' + str(int(a % y + 1)))
        a += b * (1 if pos else -1)
        pos = not pos


if __name__ == "__main__":
    # 示例：调用 main(3)
    main(3)