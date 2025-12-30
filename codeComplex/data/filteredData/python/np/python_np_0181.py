from itertools import combinations
import random

def main(n: int):
    # 生成测试数据
    # 约束示例：
    #   1 <= n
    #   c[i] 在 [1, 100] 内
    #   l, r 在可能的总和范围内
    #   x 在可能的差值范围内
    if n <= 0:
        return 0

    # 生成难度数组 c
    c = [random.randint(1, 100) for _ in range(n)]

    total_sum = sum(c)
    min_c, max_c = min(c), max(c)

    # 生成 l, r, x，确保范围合理
    l = random.randint(0, max(0, total_sum // 2))
    r = random.randint(l, total_sum)
    x = random.randint(0, max_c - min_c if max_c > min_c else 0)

    # 原逻辑：统计满足条件的方案数
    ans = 0
    for i in range(1, n + 1):
        for j in combinations(c, i):
            if max(j) - min(j) >= x and l <= sum(j) <= r:
                ans += 1

    # 可以根据需要返回结果或打印结果
    print(ans)
    return ans

if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)