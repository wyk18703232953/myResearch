def main(n):
    # 映射含义：
    # n: 数组 a 的长度
    # 其他参数 m, k 由 n 确定性生成
    # 生成方式保证可规模化且确定
    
    if n <= 0:
        # print(0)
        pass
        return

    # 让 m 与 n 成比例，但至少为 1
    m = max(1, n // 3)
    # 让 k 为一个与 n 有关的确定性值
    k = n // 5 + 1

    # 构造长度为 n 的确定性数组 a
    # 使用简单的周期与线性组合，保证数值有起伏
    a = [(i * 7 + (i % 5) * 3 - (i % 3) * 2) for i in range(n)]

    best = 0
    dp = [0] * (n + 1)
    for i in range(n):
        b2 = 0
        for j in range(max(-1, i - m), i + 1):
            segment_sum = sum(a[j + 1:i + 1]) if j + 1 <= i else 0
            b2 = max(b2, dp[j] - k + segment_sum)
        dp[i] = max(b2, a[i] - k)
        best = max(best, dp[i])

    # print(best)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 进行规模化实验
    main(10)