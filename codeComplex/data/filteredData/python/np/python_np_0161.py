from itertools import combinations
import random

def main(n):
    # 生成测试数据
    # 约束条件示例：
    #   l: 最小总和下界
    #   r: 最大总和上界
    #   x: 难度差下界
    #   a: n 个元素的数组（难度值）
    #
    # 这里使用随机生成策略，你可根据需要修改：
    #   a[i] 在 [1, 100] 内
    #   l, r, x 在合理范围内
    random.seed(0)  # 固定种子便于复现，如不需要可移除

    # 生成难度数组
    a = [random.randint(1, 100) for _ in range(n)]
    total_sum = sum(a)

    # 生成约束
    if n >= 2:
        x = random.randint(1, max(1, max(a) - min(a)))
    else:
        x = 0

    # 令 l, r 覆盖部分可行范围
    l = random.randint(0, total_sum // 2)
    r = random.randint(l, total_sum)

    # 原始逻辑
    ans = sum(
        sum(
            max(j) - min(j) >= x and l <= sum(j) <= r
            for j in combinations(a, i)
        )
        for i in range(2, n + 1)
    )

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)