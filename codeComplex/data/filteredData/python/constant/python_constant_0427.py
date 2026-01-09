def main(n):
    """
    根据规模 n 自动生成 k，并输出原程序的结果。
    原题逻辑：
        输入：n, k
        输出：根据条件计算的值
    这里依据 n 构造一个合理的 k 进行测试。
    """
    # 生成测试用的 k，可根据需要调整生成规则
    # 示例策略：让 k 在 [1, 2n] 范围内变化，这里取中间值
    k = max(1, min(2 * n, n))  # 示例：k = n（保证 1 <= k <= 2n）

    if k > n + n - 1:
        # print(0)
        pass
        return

    if k - 1 <= n:
        ml = 1
        mr = k - 1
        # print((mr - ml + 1) // 2)
        pass

    else:
        mr = n
        ml = k - n
        # print((mr - ml + 1) // 2)
        pass
if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可在此处修改 n 测试不同规模
    main(10)