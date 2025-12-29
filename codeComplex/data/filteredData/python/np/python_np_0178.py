from itertools import combinations
import random

def main(n):
    # 生成测试数据
    # 根据需要可调整生成规则
    # 这里示例：
    #   a[i] 在 1~100 之间
    #   l, r 为和的范围（较宽）
    #   x 为难度差阈值（1~50）
    a = [random.randint(1, 100) for _ in range(n)]
    l = random.randint(1, max(1, sum(a) // 4))
    r = random.randint(l, max(l + 1, sum(a) // 2))
    x = random.randint(1, 50)

    # 原逻辑
    ans = sum(
        sum(
            max(j) - min(j) >= x and l <= sum(j) <= r
            for j in combinations(a, i)
        )
        for i in range(2, n + 1)
    )

    print(ans)

if __name__ == "__main__":
    # 示例：调用 main(5)，实际使用时可在外部按需调用 main(n)
    main(5)