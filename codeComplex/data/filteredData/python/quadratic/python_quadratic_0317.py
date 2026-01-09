def main(n):
    # 这里根据 n 生成测试数据：示例为顺序整数数组 1..n，k 取 n//2 或至少为 1
    k = max(1, n // 2)
    arr = list(range(1, n + 1))

    # 前缀和
    dp = []
    x = 0
    for i in range(n):
        x += arr[i]
        dp.append(x)

    ans = 0.0
    for i in range(n):
        for j in range(i + k - 1, n):
            # (dp[j] - dp[i]) + arr[i] 等价于区间 arr[i..j] 的和
            seg_sum = (dp[j] - dp[i]) + arr[i]
            length = j - i + 1
            ans = max(ans, seg_sum / length)

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例调用：可以按需修改 n
    main(10)