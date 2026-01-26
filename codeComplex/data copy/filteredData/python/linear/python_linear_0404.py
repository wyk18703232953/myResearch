def main(n):
    # 映射规则：
    # - 原程序第一行是无用输入，忽略
    # - 第二行是单个整数 m
    # - 第三、四行各一个整数，组成两个整数的序列
    # 为了可规模化实验，仅让 n 控制 m 的大小和后续两个整数的构造
    #
    # 构造一个确定性的 m 和两个整数 a1, a2
    m = max(2, n)  # 保证不小于 2，避免除零等异常使逻辑走 except 分支
    a1 = m + 1
    a2 = 2 * m + 1

    v = m
    try:
        for a in (a1, a2):
            # 若 a == 1 会导致除零并进入 except，但在当前构造中不会发生
            v *= a / (a - 1)
    except Exception:
        v = m - 1
    result = v - m
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # 示例：使用 n = 10 运行
    main(10)