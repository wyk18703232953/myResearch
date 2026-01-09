def main(n):
    # 映射：n -> 实际的 (n, m)
    # 这里设定 m = n * 2，确保规模随 n 线性增长
    m = n * 2
    if n <= 0:
        # print(0)
        pass
        return

    # 确定性生成输入 tL0，长度为 m，元素范围在 [1, n]
    # 使用简单算术构造 (i % n) + 1
    tL0 = [(i % n) + 1 for i in range(m)]

    tL = [0] * n
    score = 0

    for i in range(m):
        tL[tL0[i] - 1] += 1
        if 0 not in tL:
            score += 1
            for j in range(n):
                tL[j] = tL[j] - 1

    # print(score)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要调整 n 的大小进行时间复杂度实验
    main(10)