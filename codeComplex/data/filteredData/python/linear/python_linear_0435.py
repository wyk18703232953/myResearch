def main(n):
    # n 为规模，这里直接使用 n 作为原题中的 n
    # 按原逻辑构造数组并返回，便于测试使用

    # 1. 计算最大 t，使得 t^2 <= n
    t = 0
    i = 1
    while True:
        k = i * i
        if k <= n:
            t = i

        else:
            break
        i += 1

    # 2. 按块大小 t 构造数组
    a = []
    z = []
    for i in range(n):
        z.append(i + 1)
        if len(z) == t:
            a = z + a
            z = []
    a = z + a
    return a


# 简单生成测试数据并打印结果示例
if __name__ == "__main__":
    # 示例：选择一个规模 n 进行测试，如 n = 10
    test_n = 10
    result = main(test_n)
    # print("n =", test_n)
    pass
    # print("result:", *result)
    pass