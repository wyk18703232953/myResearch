def main(n):
    # 这里将 n 解释为要生成的 (x, k) 测试样例对数
    # 为了示例，生成 n 组 (x, k)：x = i, k = i*i
    m = 1000000000 + 7
    results = []

    for i in range(1, n + 1):
        x = i
        k = i * i

        if x != 0:
            p1 = x * 2 - 1
            p2 = x * 2
            p = (p1 + p2) // 2
            res = (p * pow(2, k, m) + 1) % m

        else:
            res = x * 2

        results.append((x, k, res))

    # 输出每组测试数据对应的结果
    for x, k, res in results:
        # print(x, k, res)
        pass
if __name__ == "__main__":
    # 示例调用：生成 5 组 (x, k) 测试数据并计算结果
    main(5)