from itertools import combinations
import random

def main(n):
    # 根据 n 生成测试数据
    # 生成 n 个难度值，每个在 [1, 100] 范围内
    a = [random.randint(1, 100) for _ in range(n)]

    # 生成 l, r, x，确保有意义的范围
    total_sum = sum(a)
    l = random.randint(1, max(1, total_sum // 2))
    r = random.randint(l, total_sum)
    x = random.randint(0, 50)

    # 原逻辑封装
    ans = sum(
        sum(
            max(j) - min(j) >= x and l <= sum(j) <= r
            for j in combinations(a, i)
        )
        for i in range(2, n + 1)
    )
    print(ans)

if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(5)