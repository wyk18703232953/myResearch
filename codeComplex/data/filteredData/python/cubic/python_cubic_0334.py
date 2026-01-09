import sys

mod = 998244353

def main(n):
    # n 作为数组长度规模，生成一个确定性的整数数组
    a = [(i * 7 + 3) % 100000 for i in range(n)]
    a.sort()
    dp = [1] + [0] * n
    for i in range(1, n + 1):
        x, pt = 1, i - 2
        while pt >= 0 and 2 * a[pt] > a[i - 1]:
            x = x * (n - pt - 2) % mod
            pt -= 1
        dp[i] = (dp[i - 1] * (n - i) + dp[pt + 1] * x) % mod
    return dp[-1]

if __name__ == "__main__":
    # 示例调用，可按需修改 n 规模
    result = main(10)
    # print(result)
    pass