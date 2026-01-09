def main(n):
    # 这里根据 n 生成测试数据：让 k 与 n 相同
    k = n

    m = 10 ** 9 + 7
    if n:
        result = (pow(2, k, m) * (2 * n - 1) + 1) % m

    else:
        result = 0

    # print(result)
    pass
if __name__ == '__main__':
    # 示例：调用 main(10)
    main(10)