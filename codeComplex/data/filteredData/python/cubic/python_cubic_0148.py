from collections import defaultdict
import random

def main(n: int) -> int:
    # 生成规模为 n 的测试数据 X
    # 这里示例为在 [0, 2] 范围内的随机整数，可按需要修改
    random.seed(0)
    X = [random.randint(0, 2) for _ in range(n)]

    dp = defaultdict(lambda: -1)
    M = 1000001

    # 初始化 dp
    for i in range(n):
        dp[i + M] = X[i]

    # 三重循环更新 dp
    for length in range(2, n + 1):
        for start in range(n - length + 1):
            for k in range(1, length):
                u = dp[start + M * k]
                v = dp[start + k + M * (length - k)]
                if u == -1 or v == -1 or u != v:
                    continue
                dp[start + M * length] = u + 1
                break

    # 计算 dp2
    dp2 = [0] * (n + 1)
    for i in range(n):
        dp2[i + 1] = dp2[i] + 1
        for j in range(i + 1):
            if dp[j + (i + 1 - j) * M] == -1:
                continue
            dp2[i + 1] = min(dp2[i + 1], dp2[j] + 1)

    # 原程序是打印结果，这里返回结果
    return dp2[-1]


if __name__ == "__main__":
    # 示例：运行 main(5)
    ans = main(5)
    print(ans)