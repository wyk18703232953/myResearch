import itertools
import random

def main(n):
    # 生成测试数据
    # 约束：1 <= n <= 20（可根据需要修改）
    # 这里生成：
    #   problems: n 个分值在 [1, 100] 的题目
    #   l, r: 随机区间，覆盖部分可能的总和
    #   x: 难度差阈值
    random.seed(0)  # 为了结果可重复，可根据需要移除或修改

    problems = [random.randint(1, 100) for _ in range(n)]
    # 题目总和范围
    total_min = min(problems) * 2
    total_max = sum(sorted(problems, reverse=True)[:min(5, n)])  # 取最多前5个题的和，控制 r 规模
    if total_min > total_max:
        total_min, total_max = total_max, total_min

    l = random.randint(1, max(1, total_min))
    r = random.randint(l, max(l + 1, total_max))
    x = random.randint(0, max(problems) - min(problems) if n > 1 else 0)

    # 核心逻辑（原题解）
    result = 0
    for i in range(2, n + 1):
        for comb in itertools.combinations(problems, i):
            summ = sum(comb)
            mini = min(comb)
            maxx = max(comb)
            if l <= summ <= r and maxx - mini >= x:
                result += 1

    print(result)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行修改
    main(5)