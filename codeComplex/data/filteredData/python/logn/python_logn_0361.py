def main(n):
    mod = 10 ** 9 + 7

    # 生成测试数据：根据 n 构造 x, k
    # 这里简单设定：
    # x = n
    # k = n 的平方
    x = n
    k = n * n

    if x == 0:
        result = 0
    else:
        result = (pow(2, k, mod) * (2 * x - 1) + 1) % mod

    print(result)


if __name__ == '__main__':
    # 示例：可以在此修改 n 进行本地测试
    main(5)