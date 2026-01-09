def main(n: int):
    """
    n 为规模参数，这里用来生成测试数据：
    生成一对 (l, r)，约束为 0 <= l < r < 2**n。
    可根据需要调整生成策略。
    """
    if n <= 1:
        # 极小规模下，构造一个简单用例
        l, r = 0, 1

    else:
        # 生成在 [0, 2**n - 1] 范围内的一对数
        # 这里简单构造：l 为中点前一个，r 为中点后一个
        max_val = (1 << n) - 1
        mid = max_val // 2
        l = max(0, mid - 1)
        r = min(max_val, mid + 1)
        if l == r:
            r = min(max_val, l + 1)

    # 原始逻辑
    if l == r:
        ans = 0

    else:
        ans = (1 << len(bin(l ^ r)[2:])) - 1

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10) 可运行一次
    main(10)