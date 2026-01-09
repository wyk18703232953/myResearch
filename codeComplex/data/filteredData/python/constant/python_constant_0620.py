def main(n):
    # 生成规模为 n 的测试数据：构造 n 个区间 [l, r]
    # 这里示例生成 [1,1], [1,2], ..., [1,n]
    Q = n
    LR = [[1, i] for i in range(1, n + 1)]

    # 原有逻辑中的 SUM 函数
    def SUM(i):
        plus = i // 2
        minus = (i + 1) // 2

        P = (2 + 2 * plus) * plus // 2
        M = (1 + 2 * minus - 1) * minus // 2
        return P - M

    # 执行查询并打印结果
    for l, r in LR:
        # print(SUM(r) - SUM(l - 1))
        pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)