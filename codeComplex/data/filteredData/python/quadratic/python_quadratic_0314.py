import random

def main(n: int) -> float:
    # 生成测试数据：随机选择 k，随机生成长度为 n 的数组 arr
    if n <= 0:
        return 0.0

    # k 至少为 1，至多为 n
    k = random.randint(1, n)

    # 生成数组元素，这里使用 [-10^3, 10^3] 区间的整数作为示例
    arr = [random.randint(-1000, 1000) for _ in range(n)]

    # 前缀和数组
    x = 0
    dp = []
    for i in range(n):
        x += arr[i]
        dp.append(x)

    # 计算答案
    ans = float("-inf")
    for i in range(n):
        for j in range(i + k - 1, n):
            # 区间 [i, j] 的和为 dp[j] - dp[i] + arr[i]
            current_sum = dp[j] - dp[i] + arr[i]
            length = j - i + 1
            ans = max(ans, current_sum / length)

    return ans

if __name__ == "__main__":
    # 示例：调用 main(10) 并打印结果
    result = main(10)
    print(result)