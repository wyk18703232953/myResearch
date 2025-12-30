from itertools import combinations
import random

def main(n):
    # 1. 生成测试数据
    # 约束条件：1 <= l <= r，x 为需要的最小难度差
    # 随机生成难度数组 a，值适中以便组合数量可控
    random.seed(0)  # 固定种子，保证复现性

    # 生成 n 个题目的难度
    a = [random.randint(1, 100) for _ in range(n)]

    # 为了保证有一定可行性，基于 a 构造 l, r, x
    total_sum = sum(a)
    min_a, max_a = min(a), max(a)

    # x 取整体跨度的一部分
    x = max(1, (max_a - min_a) // 3)

    # l, r 取总和的某个区间，这里取大约 [总和的 1/4, 3/4]
    l = total_sum // 4
    r = (total_sum * 3) // 4
    if l == 0:
        l = 1
    if l > r:
        l, r = r, l

    # 2. 按原逻辑计算答案
    arr = []
    for i in range(2, n + 1):
        for comb in combinations(a, i):
            arr.append(list(comb))

    count = 0
    for subset in arr:
        dif = max(subset) - min(subset)
        total = sum(subset)
        if dif >= x and l <= total <= r:
            count += 1

    print(count)

if __name__ == "__main__":
    # 示例：调用 main，规模 n 可根据需要修改
    main(10)