import sys

def main(n):
    # 映射：n 既作为数组长度，也作为 k 的规模参数
    if n <= 0:
        # print(0.0)
        pass
        return

    # 确定性生成 n 与 k
    length = n
    k = max(1, n // 3)  # 保证有一定窗口大小，但不超过 n
    if k > length:
        k = length

    # 确定性生成数组 arr，依赖 n
    # 例如：arr[i] = (i * 7 + n) % (n + 5) + 1，确保为正数
    arr = [((i * 7 + n) % (n + 5)) + 1 for i in range(length)]

    x = 0
    dp = []
    for i in range(length):
        x = x + arr[i]
        dp.append(x)

    ans = 0.0
    for i in range(length):
        for j in range(i + k - 1, length):
            s = (dp[j] - dp[i]) + arr[i]
            avg = s / (j - i + 1)
            if avg > ans:
                ans = avg

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 进行时间复杂度实验
    main(1000)