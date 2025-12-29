import itertools
import random

def main(n):
    # 生成测试数据
    # 随机生成题目难度 problems，值在 1~1000 之间
    random.seed(0)  # 固定随机种子，便于复现
    problems = [random.randint(1, 1000) for _ in range(n)]

    # 生成约束参数 l, r, x
    total_sum = sum(problems)
    l = total_sum // 4
    r = total_sum // 2
    x = max(1, (max(problems) - min(problems)) // 3)

    ans = 0
    for i in range(2, n + 1):
        for j in itertools.combinations(problems, i):
            if l <= sum(j) <= r and max(j) - min(j) >= x:
                ans += 1

    print(ans)


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)