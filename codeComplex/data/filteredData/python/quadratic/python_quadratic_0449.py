def main(n):
    if n <= 0:
        return

    # 确定性生成输入数组 arr，长度为 n
    # 使用简单的周期模式，包含上升、下降和相等的情况
    base = [1, 2, 2, 3, 1]
    arr = [base[i % len(base)] + (i // len(base)) for i in range(n)]

    dp = [[0] * 5 for _ in range(n)]
    dp[0] = [1, 1, 1, 1, 1]

    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            for j in range(1, 5):
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 1])
        elif arr[i] < arr[i - 1]:
            for j in range(3, -1, -1):
                dp[i][j] = max(dp[i - 1][j + 1], dp[i][j + 1])

        else:
            s = sum(dp[i - 1])
            for j in range(5):
                dp[i][j] += (s > 0) * (dp[i - 1][j] == 0 or s > 1)

    if dp[-1] == [0, 0, 0, 0, 0]:
        # print(-1)
        pass

    else:
        ans = [dp[-1].index(1) + 1]
        for i in range(n - 2, -1, -1):
            for j in range(5):
                if dp[i][j] > 0 and (
                    (j + 1 > ans[-1] and arr[i] > arr[i + 1])
                    or (j + 1 < ans[-1] and arr[i] < arr[i + 1])
                    or (j + 1 != ans[-1] and arr[i] == arr[i + 1])
                ):
                    ans.append(j + 1)
                    break
        # print(*reversed(ans))
        pass
if __name__ == "__main__":
    # 示例规模调用，可根据需要调整 n 进行时间复杂度实验
    main(10)