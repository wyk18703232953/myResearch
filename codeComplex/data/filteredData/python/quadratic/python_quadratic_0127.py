def main(n):
    # 映射：n -> n (数组长度)，m = n // 2（窗口长度，保证 m <= n）
    if n <= 0:
        return
    m = max(1, n // 2)

    # 生成确定性数组 l，长度为 n
    # 这里构造重复元素，以保证有意义的计数操作
    l = [(i * 3) % (n // 2 + 1) for i in range(n)]

    # 原程序核心逻辑
    d = dict()
    if len(set(l)) < n:
        # print(0)
        pass

    else:
        for i in range(m):
            d.setdefault(l[i], 0)
            d[l[i]] += 1
        min1 = 999999999
        for i in d.values():
            if i < min1:
                min1 = i
        # print(min1)
        pass
if __name__ == "__main__":
    main(1000)