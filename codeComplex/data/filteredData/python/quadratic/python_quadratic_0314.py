def main(n):
    # 映射：给定 n，构造 k 和长度为 n 的数组 arr
    if n <= 0:
        return 0.0

    # 合理选择 k，使其随 n 变化但始终不超过 n
    # 这里设定 k = max(1, n // 3)
    k = n // 3
    if k < 1:
        k = 1
    if k > n:
        k = n

    # 确定性生成数组 arr，长度为 n
    # 使用简单的算术构造：arr[i] = (i * 3 + 1) % 10 + 1
    arr = [((i * 3 + 1) % 10) + 1 for i in range(n)]

    x = 0
    dp = []
    for i in range(n):
        x = x + arr[i]
        dp.append(x)

    ans = 0.0
    for i in range(n):
        for j in range(i + k - 1, n):
            current = ((dp[j] - dp[i]) + arr[i]) / (j - i + 1)
            if current > ans:
                ans = current
    return ans


if __name__ == "__main__":
    # 示例调用，可以修改 n 以做不同规模的实验
    result = main(10)
    # print(result)
    pass