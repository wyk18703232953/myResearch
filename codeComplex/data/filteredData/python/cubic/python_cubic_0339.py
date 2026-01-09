import sys

mod = 998244353

def main(n):
    # 生成确定性输入：长度为 n 的整数数组 a
    # 这里选择 a[i] = (i * 2 + 1) % (3 * n + 1)，保证有序性后仍有一定分布
    if n <= 0:
        # print(0)
        pass
        return

    a = [(i * 2 + 1) % (3 * n + 1) for i in range(n)]
    a.sort()

    dp = [1] + [0] * n
    for i in range(1, n + 1):
        x, pt = 1, i - 2
        while pt >= 0 and 2 * a[pt] > a[i - 1]:
            x = x * (n - pt - 2) % mod
            pt -= 1
        dp[i] = (dp[i - 1] * (n - i) + dp[pt + 1] * x) % mod
    # print(dp[-1])
    pass
if __name__ == "__main__":
    # 示例调用，可按需修改 n 的大小进行复杂度实验
    main(10)