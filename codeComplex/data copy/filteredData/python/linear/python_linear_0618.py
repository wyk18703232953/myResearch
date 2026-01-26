def main(n):
    # 输入结构分析：
    # 原程序：
    # n
    # a1 a2 ... an
    # b1 b2 ... bn
    #
    # a, b 显然是 1..n 的排列（从索引访问和减 1 可推断）
    # 为了可规模化、确定性、可重复：
    # - 令 a 为 1..n 的顺序排列
    # - 令 b 为一个确定性的“扰动”排列：通过简单算术映射生成
    #
    # 这里选择：
    # a = [1, 2, ..., n]
    # b[i] = ((i * 2 + 3) % n) + 1  （1 <= i <= n），再打散避免周期过短模式
    # 为保持简单又有规律，直接使用该公式生成一个置换并调整重复。

    if n <= 0:
        # print()
        pass
        return

    # 生成 a：严格递增的 1..n
    a = list(range(1, n + 1))

    # 初始生成一个可能有重复的序列
    raw_b = [((i * 2 + 3) % n) + 1 for i in range(n)]

    # 将 raw_b 映射成一个确定性的置换：
    # 规则：按 raw_b 的顺序遍历可选数字池，依次选取第 (raw_b[i]-1) mod 剩余长度 个元素
    pool = list(range(1, n + 1))
    b = []
    for i in range(n):
        idx = (raw_b[i] - 1) % len(pool)
        b.append(pool.pop(idx))

    # 下面是原始算法逻辑（仅把输入替换为上述确定性生成的 a, b）
    a = a[::-1]
    c = [0] * n
    bk = []
    for i in range(n):
        co = 0
        if c[b[i] - 1] == 0:
            while a and a[-1] != b[i]:
                co += 1
                c[a[-1] - 1] = 1
                a.pop()
            if a:
                co += 1
                c[a[-1] - 1] = 1
                a.pop()
        bk.append(co)
    # print(*bk)
    pass
if __name__ == "__main__":
    # 示例调用：可以自行修改 n 观察时间复杂度变化
    main(5)