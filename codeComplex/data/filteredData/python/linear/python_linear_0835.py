from collections import deque
import random

def main(n):
    # 随机生成测试数据规模：
    # n: 字符串长度
    # m: 区间长度，取 1~n 之间的随机值
    # s: 长度为 n 的随机 RGB 字符串
    #
    # 原程序有多组用例，这里生成 1 组用例进行演示
    c = 1
    print("Number of test cases:", c)

    # 生成并处理 c 个测试用例
    for cas in range(c):
        # 生成 n, m, s
        m = random.randint(1, n)  # 1 ≤ m ≤ n
        chars = ['R', 'G', 'B']
        s = deque(random.choice(chars) for _ in range(n))

        print(f"Test case {cas + 1}:")
        print("n =", n, ", m =", m)
        print("s =", ''.join(s))

        arr = ["R", "G", "B"]
        ans = n + 3  # 上界

        # 原代码 for k in range(1): 没有实际作用，这里保留逻辑不变
        for _ in range(1):
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

        print("Answer:", ans)


# 示例：当作为脚本运行时，可调用 main(n)
if __name__ == "__main__":
    main(10)