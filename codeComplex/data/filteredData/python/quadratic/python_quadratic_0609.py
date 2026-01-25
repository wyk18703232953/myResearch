import math

def max_sub(arr, n):
    dp = [0] * n
    dp[0] = arr[0]
    for i in range(1, n):
        dp[i] = max(dp[i - 1] + arr[i], arr[i])
    return max(0, max(dp))

def main(n):
    # 规模含义：
    # n: 数组长度
    # m: 分段数量，固定为 3（对应原始示例）
    # k: 固定成本，设为 10（对应原始示例）
    if n <= 0:
        return

    m = 3
    k = 10

    # 确定性生成数组：
    # 模仿原示例 [1, 2, 10, 2, 3] 的模式：
    # arr[i] = (i * 7) % 13 + 1
    arr = [(i * 7) % 13 + 1 for i in range(n)]

    q = -math.inf
    dp = [0] * 300100
    for i in range(300100):
        dp[i] = [q] * 11

    if m == 1:
        for i in range(n):
            arr[i] = arr[i] - k
        print(max_sub(arr, n))
    else:
        for i in range(n):
            dp[i][1] = arr[i] - k
            for j in range(m):
                if i - 1 < 0 or dp[i - 1][j] == q:
                    continue
                if (j + 1) % m != 1:
                    dp[i][(j + 1) % m] = dp[i - 1][j] + arr[i]
                else:
                    dp[i][(j + 1) % m] = max(arr[i] - k, dp[i - 1][j] + arr[i] - k)
        ma = 0
        for i in range(n):
            for j in range(m):
                ma = max(ma, dp[i][j])
        print(ma)

if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 来进行不同规模的实验
    main(5)