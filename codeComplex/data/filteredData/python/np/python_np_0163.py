import random

c = 0

def backtracking(actuales, restantes, l, r, x):
    global c
    s = sum(actuales)
    if l <= s <= r:
        if max(actuales) - min(actuales) >= x:
            c += 1
    if restantes:
        for i in range(len(restantes)):
            backtracking(actuales + [restantes[i]], restantes[i + 1:], l, r, x)
    return 0

def main(n):
    """
    n: 题目数量规模（生成 n 个难度值）
    返回：满足条件的方案数
    """
    global c
    c = 0

    # 根据 n 生成测试数据
    # 难度值范围可自行调整，这里设为 [1, 1000]
    difficulties = [random.randint(1, 1000) for _ in range(n)]
    difficulties.sort()

    # 生成约束参数 l, r, x，保证一定合理性
    total_sum = sum(difficulties)
    l = total_sum // 4 if total_sum >= 4 else 0
    r = total_sum
    x = max(1, (max(difficulties) - min(difficulties)) // 3)

    backtracking([], difficulties, l, r, x)
    return c

if __name__ == "__main__":
    # 示例：n=10
    print(main(10))