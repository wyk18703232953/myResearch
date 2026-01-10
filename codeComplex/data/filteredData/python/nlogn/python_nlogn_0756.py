def main(n):
    # n 表示测试用例数量 t
    t = n

    # 为每个测试用例生成一个规模随用例编号线性增长的数组
    # 第 i 个测试用例的 n_i = i + 3，保证 n_i >= 3 以确保 a[1] 存在
    # 数组元素通过简单算术构造，确保确定性
    for i in range(t):
        n_i = i + 3
        a = [((j * 7 + 3) % (n_i * 3) + 1) for j in range(n_i)]
        a.sort(reverse=True)
        print(min(n_i - 2, a[1] - 1))


if __name__ == "__main__":
    main(10)