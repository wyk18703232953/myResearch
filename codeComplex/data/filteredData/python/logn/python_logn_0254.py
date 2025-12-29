def main(n):
    # 生成测试数据：根据规模 n 构造 (x, k)
    # 这里简单示例：x = n, k = n 的平方
    x = n
    k = n * n

    m = 10**9 + 7
    if x == 0:
        print(0)
    else:
        print((pow(2, k + 1, m) * x - pow(2, k, m) + 1) % m)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)