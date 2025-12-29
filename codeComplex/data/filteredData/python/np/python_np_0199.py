from itertools import combinations
import random

def main(n: int):
    # 1. 生成测试数据
    # 约定：
    #   a[i] 在 [1, 100] 范围内
    #   l, r 为总和区间，l 在可能总和范围内，r >= l
    #   x 为难度差阈值
    random.seed(0)  # 如需随机性，可去掉这一行

    # 生成难度数组 a
    a = [random.randint(1, 100) for _ in range(n)]

    # 总和范围
    total_min = min(a) * 2
    total_max = sum(a)

    if total_min > total_max:
        l, r = 0, 0
    else:
        l = random.randint(total_min, total_max)
        r = random.randint(l, total_max)

    # 差值阈值 x
    if n >= 2:
        x = random.randint(0, max(a) - min(a))
    else:
        x = 0

    # 2. 原逻辑计算
    ans = sum(
        sum(
            max(j) - min(j) >= x and l <= sum(j) <= r
            for j in combinations(a, i)
        )
        for i in range(2, n + 1)
    )

    print(ans)

if __name__ == "__main__":
    # 示例：运行 main(5)
    main(5)