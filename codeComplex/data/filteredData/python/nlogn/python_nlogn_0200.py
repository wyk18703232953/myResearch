from collections import deque
import heapq
import random


def main(n):
    # 1. 生成测试数据
    # 设定总时间上限 T，和 n 个题目的 (a, t)
    # a: 题目价值（至少要 >= K 才能考虑），t: 完成时间
    # 这里随机构造，可根据需要调整数据范围
    random.seed(0)
    T = n * 10  # 总时间上限
    problems = []
    for _ in range(n):
        a = random.randint(0, n)      # 价值 0..n
        t = random.randint(1, 20)     # 完成时间 1..20
        problems.append((a, t))

    def possible(K):
        d = []
        for a, t in problems:
            if a >= K:
                d.append(t)
        d.sort()
        if len(d) < K:
            return False
        else:
            return sum(d[:K]) <= T

    # 2. 二分答案
    l = 0
    r = n + 1
    while r - l > 1:
        med = (r + l) // 2
        if possible(med):
            l = med
        else:
            r = med

    # 3. 输出与原逻辑一致的结果
    print(l)
    print(l)
    d = []
    for i, (a, t) in enumerate(problems):
        if a >= l:
            d.append((t, i + 1))
    d.sort(key=lambda x: x[0])
    ans = [v[1] for v in d[:l]]
    if ans:
        print(*ans)
    else:
        print()


# 示例调用
if __name__ == "__main__":
    main(10)