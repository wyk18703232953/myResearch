def main(n):
    import sys

    # 规模含义：
    # n 为数组长度，生成确定性的 l, c
    # l: 严格递增保证存在可行三元组（除去尾部一些扰动保持多样性）
    # c: 简单确定性代价模式
    if n < 3:
        # print(-1)
        pass
        return

    # 生成 l: 前半部分递增，后半部分做一些小幅变化但仍大致递增
    l = [i for i in range(1, n + 1)]
    # 加一点确定性的扰动（保持确定性）
    for i in range(n):
        if i % 5 == 0:
            l[i] += (i // 5)

    # 生成 c: 与下标相关的确定性模式
    c = [(i * 3 + 7) % 100 + 1 for i in range(n)]

    a = []
    for i in range(1, n - 1):
        lr = sys.maxsize
        lc = sys.maxsize
        for j in range(0, i):
            if l[i] > l[j]:
                if c[j] < lc:
                    lc = c[j]
        for j in range(i + 1, n):
            if l[j] > l[i]:
                if c[j] < lr:
                    lr = c[j]
        if lr < sys.maxsize and lc < sys.maxsize:
            a.append(lr + lc + c[i])
    if not a:
        # print(-1)
        pass

    else:
        # print(min(a))
        pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 来做规模实验
    main(10)