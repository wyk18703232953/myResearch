def check_combos(diff, n, size, start, picked, total, l, r, x, combination=None):
    if combination is None:
        combination = []
    if picked == size:
        if max(combination) - min(combination) >= x and l <= sum(combination) <= r:
            total += 1

    else:
        # 循环上界修正为 n - (size - picked) + 1 以保证区间非空
        for i in range(start, n - (size - picked) + 1):
            combination.append(diff[i])
            total = check_combos(diff, n, size, i + 1, picked + 1, total, l, r, x, combination)
            combination.pop()
    return total


def main(n):
    """
    n: 题目数量规模，用于生成测试数据
    测试数据生成策略（示例）：
      diff: 1, 2, ..., n
      l = n          （最小总难度）
      r = n * (n + 1) // 2  （最大可能总难度）
      x = 1          （最小难度差）
    """
    # 生成测试数据（可按需求修改生成策略）
    diff = list(range(1, n + 1))
    l = n
    r = n * (n + 1) // 2
    x = 1

    suitable_problemsets = 0
    for size in range(1, n + 1):
        suitable_problemsets += check_combos(diff, n, size, 0, 0, 0, l, r, x)
    # print(suitable_problemsets)
    pass


# 示例调用
if __name__ == "__main__":
    main(5)