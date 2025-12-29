import math as mt
import itertools as it
import random

def main(n):
    # 生成测试数据
    # n: 题目中题意的 n（题目数量）
    # a: 长度为 n 的难度数组，每个在 [1, 100] 内
    # l, r, x: 约束参数
    random.seed(0)  # 如需每次不同数据可移除此行

    a = [random.randint(1, 100) for _ in range(n)]
    l = n * 10            # 示例：最小和
    r = n * 60            # 示例：最大和
    x = max(1, n // 3)    # 示例：最小难度差

    ans = 0
    for j in range(2, n + 1):
        for comb in it.combinations(a, j):
            if max(comb) - min(comb) >= x and l <= sum(comb) <= r:
                ans += 1
    print(ans)


if __name__ == "__main__":
    # 示例运行：可修改 n 进行不同规模测试
    main(5)