from itertools import chain, combinations
import random

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

def diff(s, x):
    return True if (max(s) - min(s)) >= x else False

def solve(problemset, l, r, x):
    multiset = powerset(problemset)
    cnt = 0
    for s in multiset:
        if len(s) == 0:
            continue  # 原代码中空集合不会通过 diff 条件，但这里直接跳过更安全
        if l <= sum(s) <= r and diff(s, x):
            cnt += 1
    return cnt

def main(n: int):
    # 根据 n 生成测试数据
    # n: 题目数量规模
    # l, r: 总难度区间
    # x: 难度差阈值
    random.seed(0)

    # 难度值在 1~1000 之间
    problemset = [random.randint(1, 1000) for _ in range(n)]

    # 根据题目总和的大致范围生成 l, r
    total_sum = sum(problemset)
    # 防止范围过大/过小，做一个合理缩放
    l = total_sum // 4
    r = total_sum // 2
    if l == 0:
        l = 1
    if r < l:
        r = l

    # x 为难度差，取一个相对不太小的值
    x = max(1, (max(problemset) - min(problemset)) // 4)

    ans = solve(problemset, l, r, x)
    print(ans)

if __name__ == "__main__":
    # 示例：调用 main，规模可按需调整
    main(10)