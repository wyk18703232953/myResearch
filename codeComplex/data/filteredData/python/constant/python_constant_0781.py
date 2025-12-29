def main(n):
    # 预处理可行的数值集合 k
    k = set()
    upper = 10**5
    for i in range(1, upper):
        k.add(4 * i * i)
        k.add(2 * i * i)

    # 根据规模 n 生成测试数据：
    # 这里简单生成前 n 个整数作为待检测的数列，
    # 你可以根据需要修改生成方式。
    test_values = list(range(1, n + 1))

    # 对每个测试值进行判断并输出结果
    for val in test_values:
        if val in k:
            print('YES')
        else:
            print('NO')


if __name__ == "__main__":
    # 示例：调用 main(10)，可根据需要修改规模
    main(10)