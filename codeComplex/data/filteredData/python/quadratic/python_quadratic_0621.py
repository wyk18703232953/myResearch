def main(n):
    # 映射含义：
    # n -> 数组 a 的长度
    # m, k 与 n 通过确定性方式设定，保持可规模化和确定性
    if n <= 0:
        # print(0)
        pass
        return

    # 确定性构造 m 和 k，使其随 n 变化但不依赖外部输入
    m = max(1, n // 3)  # 确保 1 <= m <= n
    k = n // 5 + 1

    # 确定性生成数组 a，长度为 n
    # 使用简单算术构造，使得既有正数也有负数，便于算法运行
    a = [((i * 2) % 7) - 3 for i in range(1, n + 1)]

    dp = [-1] * (n + 15)
    for i in range(n):
        s = a[i]
        mx = max(0, a[i])
        for j in range(i - 1, max(-1, i - m), -1):
            s += a[j]
            mx = max(mx, s)
        dp[i] = max(0, (dp[i - m] if i - m >= 0 else 0) + s - k, mx - k)
    # print(max(dp))
    pass
if __name__ == "__main__":
    # 示例：运行若干不同规模，方便做时间复杂度实验
    for size in [10, 100, 1000]:
        main(size)