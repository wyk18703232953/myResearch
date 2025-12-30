from itertools import combinations
import random

def main(n: int):
    # 生成测试数据
    # 题意要求：有 n 个数，约束 l, r, x
    # 这里给出一种合理的随机测试数据生成方案：
    #   a[i] 在 [1, 100] 内
    #   l, r 为和的区间，l <= r
    #   x 为最大值与最小值的最小差值
    #
    # 你可以根据需要调整下面的生成策略。
    a = [random.randint(1, 100) for _ in range(n)]
    l = random.randint(1, max(1, 20))
    r = random.randint(l, 200)  # 保证 r >= l
    x = random.randint(0, 50)

    # 原逻辑：统计满足条件的题目集合数量
    ans = sum(
        sum(
            max(j) - min(j) >= x and l <= sum(j) <= r
            for j in combinations(a, i)
        )
        for i in range(2, n + 1)
    )

    print(ans)

if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行调整
    main(5)