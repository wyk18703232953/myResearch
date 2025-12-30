import math
import random

def main(n):
    # 生成测试数据：
    # n: 字符串长度
    # 随机生成 k (1 <= k <= n)
    # 随机生成只包含 'R' 'G' 'B' 的字符串 s
    k = random.randint(1, n)
    s = ''.join(random.choice('RGB') for _ in range(n))

    rgb = 'RGB'
    ans = math.inf

    for start in range(3):
        dp = [0] * (n + 1)
        for i in range(n):
            cur = rgb[(start + i) % 3]
            dp[i + 1] = dp[i] + int(s[i] != cur)
        for i in range(n - k + 1):
            ans = min(ans, dp[i + k] - dp[i])

    # 按原程序行为：打印结果
    print(ans)

# 示例调用
if __name__ == "__main__":
    main(10)