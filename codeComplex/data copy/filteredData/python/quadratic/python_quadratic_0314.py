def main(n):
    # 映射 n 为原程序中的 n，固定 k 为 5（可根据需要调整）
    if n <= 0:
        # print(0.0)
        pass
        return
    k = 5
    if k > n:
        k = n

    # 确定性生成数组 arr，长度为 n
    # 例如：arr[i] = (i * 2 + 3) % 100 + 1
    arr = [((i * 2 + 3) % 100) + 1 for i in range(n)]

    x = 0
    dp = []
    for i in range(n):
        x = x + arr[i]
        dp.append(x)

    ans = 0.0
    for i in range(n):
        for j in range(i + k - 1, n):
            val = ((dp[j] - dp[i]) + arr[i]) / (j - i + 1)
            if val > ans:
                ans = val
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的规模
    main(10)