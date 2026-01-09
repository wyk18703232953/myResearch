def main(n):
    import sys

    # 确定性生成输入
    # N 为输入规模
    N = max(1, n)

    # 生成长度为 N 的整数数组 za
    # 设计为含有正数、负数和零（除非 N 太小）
    za = []
    for i in range(N):
        # 生成有正有负有零的整数序列
        # 分布范围随 N 线性增长，保持可规模化
        val = (i * 2 - N)  # 从约 -N 到 N 的线性序列
        za.append(val)

    # 原算法逻辑开始
    if N == 1:
        # print(za[0])
        pass
        return

    t1 = max(za)
    t2 = min(za)
    if t2 >= 0:
        # print(sum(za) - 2 * t2)
        pass
        return
    if t1 <= 0:
        # print(2 * t1 - sum(za))
        pass
        return

    res = 0
    for x in za:
        res += abs(x)

    # print(res)
    pass
if __name__ == "__main__":
    # 示例：以 n = 10 作为输入规模运行
    main(10)