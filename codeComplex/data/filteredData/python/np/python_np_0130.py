from collections import defaultdict
from math import gcd
import random


def main(n: int):
    # 生成测试数据：
    # 这里生成长度为 n 的数组 A, B，元素为 1~10^6 之间的正整数
    # 可根据需要调整生成策略
    max_val = 10**6
    A = [random.randint(1, max_val) for _ in range(n)]
    B = [random.randint(1, max_val) for _ in range(n)]

    dp = defaultdict(lambda: float("inf"))
    for a, b in zip(A, B):
        # 更新当前 a 的最小代价
        dp[a] = min(dp[a], b)
        # 遍历当前已有的所有 gcd 状态
        current_dp_items = list(dp.items())
        for d, cost_d in current_dp_items:
            cur = gcd(a, d)
            dp[cur] = min(dp[cur], dp[a] + cost_d)

    if 1 not in dp or dp[1] == float("inf"):
        print(-1)
    else:
        print(dp[1])


if __name__ == "__main__":
    # 示例：运行规模 n=5
    main(5)