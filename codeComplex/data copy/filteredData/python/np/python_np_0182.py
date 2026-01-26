def subsets(S):
    sets = []
    len_S = len(S)
    for i in range(1 << len_S):
        subset = [S[bit] for bit in range(len_S) if i & (1 << bit)]
        sets.append(subset)
    return sets


def main(n):
    # 生成规模为 n 的测试数据
    # 这里示例：problems 为 1..n 的整数，
    # l 为前一半的和，r 为全部的和，x 为 1
    problems = list(range(1, n + 1))
    total_sum = sum(problems)
    l = total_sum // 2
    r = total_sum
    x = 1

    res = 0
    for m in subsets(problems):
        if len(m) == 0:
            continue
        s = sum(m)
        if l <= s <= r and (max(m) - min(m)) >= x:
            res += 1
    # print(res)
    pass
if __name__ == "__main__":
    # 示例：调用 main，规模 n 可在此修改
    main(5)