from collections import deque
import random

def main(n):
    """
    n: 字符串长度规模
    自动生成：
    - m: 1 到 n 之间的随机窗口长度
    - s: 长度为 n 的随机 'R','G','B' 字符串
    输出：最小修改次数
    """
    # 生成测试数据
    # 可按需要自行指定 m 和 s，这里给一个简单随机生成方式
    m = random.randint(1, n)
    chars = ['R', 'G', 'B']
    s = deque(random.choice(chars) for _ in range(n))

    arr = ["R", "G", "B"]
    ans = n + 3

    # 原代码中外层 for k in range(1) 仅循环一次，可直接去掉
    for i in range(3):
        x = i
        dp = [0] * (n + 1)
        for j in range(n):
            if s[j] != arr[x]:
                dp[j + 1] += 1
            dp[j + 1] += dp[j]
            if j + 1 >= m:
                ans = min(ans, dp[j + 1] - dp[j + 1 - m])
            x = (x + 1) % 3

    print(ans)


if __name__ == "__main__":
    # 示例调用：n = 10
    main(10)