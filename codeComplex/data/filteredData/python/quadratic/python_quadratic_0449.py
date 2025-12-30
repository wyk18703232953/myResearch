import random

def main(n: int):
    # 生成规模为 n 的测试数据，这里使用 1~100 的随机整数
    if n <= 0:
        return
    arr = [random.randint(1, 100) for _ in range(n)]

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
    # 示例调用：n = 10
    main(10)