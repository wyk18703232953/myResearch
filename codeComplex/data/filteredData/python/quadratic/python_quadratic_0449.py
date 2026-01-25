def main(n):
    # n 表示序列长度
    if n <= 0:
        return

    # 确定性生成数组 arr，长度为 n
    # 模式：前 1/3 严格递增，中间 1/3 保持不变，后 1/3 严格递减
    arr = [0] * n
    for i in range(n):
        if n == 1:
            arr[i] = 1
        else:
            if i < n // 3:
                arr[i] = i
            elif i < 2 * n // 3:
                arr[i] = n // 3
            else:
                arr[i] = 2 * n // 3 - (i - 2 * n // 3)

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
        print(-1)
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
        print(*reversed(ans))


if __name__ == "__main__":
    main(10)