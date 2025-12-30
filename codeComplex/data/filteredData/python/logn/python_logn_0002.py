def main(n):
    # 根据规模 n 生成测试数据
    # 这里简单设定 a = n, b = 2 * n，保证一般情况下 a != b
    a = n
    b = 2 * n

    if a == b:
        print(0)
    else:
        x = a ^ b
        c = 0
        while x:
            x = x // 2
            c += 1
        print(2 ** c - 1)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)