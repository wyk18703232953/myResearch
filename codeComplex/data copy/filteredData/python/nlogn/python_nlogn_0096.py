def main(n):
    # n 表示 complexity 列表的长度
    # 为保证索引 chores[2] 和 chores[2]-1 有效，需 n >= 2
    if n < 2:
        # print(0)
        pass
        return

    # 构造确定性的 chores 列表，规模与原程序含义一致
    # chores[2] 将作为索引使用，因此限制在 [1, n-1]
    chores = [0, 1, min(2, n - 1)]

    # 构造确定性的 complexity 列表，长度为 n
    complexity = [(i * 3 + 1) for i in range(n)]

    # 核心逻辑保持不变
    complexity.sort()
    idx = chores[2]
    result = complexity[idx] - complexity[idx - 1]
    # print(result)
    pass
if __name__ == "__main__":
    main(10)