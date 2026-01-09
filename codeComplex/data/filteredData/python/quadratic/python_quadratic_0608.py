def main(n: int):
    base = 1000000007
    # 这里根据 n 生成测试数据，你可以按需要修改生成规则
    # 示例：m 取 1~n 中某个值（这里取 n 的一半，至少为 1），k 固定为 1
    m = max(1, n // 2)
    k = 1
    # 生成长度为 n 的数组 a，这里用简单的递增序列作为示例测试数据
    a = [i + 1 for i in range(n)]

    mx = 0
    dp = []
    dd = []

    for j in range(m):
        # 每轮 j 重新扩展 dp 和 dd 的空间
        for _ in range(n + 1):
            dp.append(base)
            dd.append(0)
        # 当前这轮在 dp、dd 中的起始偏移量
        offset = j * (n + 1)

        # 初始化这一轮对应的 dp、dd
        dp[offset] = base
        dd[offset] = 0

        for i in range(n):
            idx_prev = offset + i
            idx_curr = offset + i + 1
            dd[idx_curr] = dd[idx_prev] + a[i] - k * (i % m == j)
            dp[idx_curr] = min(dd[idx_prev], dp[idx_prev])
            if i % m == j:
                mx = max(mx, dd[idx_curr] - dp[idx_curr])

    # print(mx)
    pass
if __name__ == "__main__":
    # 示例调用：n=10
    main(10)