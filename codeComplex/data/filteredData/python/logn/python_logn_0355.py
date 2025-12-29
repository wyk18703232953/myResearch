def main(n):
    # n 作为规模参数，这里用来构造测试数据：
    # 比如让 x = n, k = n 的平方
    x = n
    k = n * n

    md = 1000000007
    if x > 0:
        result = (pow(2, k + 1, md) * x - pow(2, k, md) + 1) % md
    else:
        result = 0

    print(result)


if __name__ == "__main__":
    # 示例：可以在此处手动指定 n 进行测试
    main(10)