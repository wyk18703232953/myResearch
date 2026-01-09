def main(n: int):
    # 根据 n 生成测试数据：这里直接使用 n 作为规模参数
    m = int(n ** 0.5)
    a = []

    for i in range(0, n, m):
        for j in range(i, min(i + m, n)):
            a.append(min(i + m, n) - j + i)

    # print(' '.join(str(x) for x in a))
    pass
if __name__ == "__main__":
    # 示例：调用 main，使用某个规模 n 进行测试
    test_n = 100
    main(test_n)