def subsets(L, i):
    if i == len(L):
        yield []

    else:
        for s in subsets(L, i + 1):
            yield s
            yield [L[i]] + s

def computeValidProblemsets(problems, l, r, x):
    isValid = lambda ps: (len(ps) > 1) and (l <= sum(ps) <= r) and (ps[-1] - ps[0] >= x)
    return sum(isValid(problemset) for problemset in subsets(sorted(problems), 0))

def main(n):
    # 根据规模 n 生成测试数据：
    # 生成 n 个题目难度，简单起见设为 1, 2, ..., n
    problems = list(range(1, n + 1))

    # 设置参数 l, r, x（可按需要修改生成策略）
    l = n          # 最小难度和
    r = n * (n + 1) // 2  # 最大难度和设为所有题目之和
    x = 1          # 最小难度差

    ans = computeValidProblemsets(problems, l, r, x)
    # print(ans)
    pass
if __name__ == '__main__':
    # 示例运行：可以修改 n 测试不同规模
    main(5)