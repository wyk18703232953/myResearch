def main(n):
    # n 表示输入规模，这里映射为：
    # n = 数列长度 = m
    # n = 需要统计的前缀长度
    if n <= 0:
        # print(0)
        pass
        return

    # 构造确定性的 n 和 m
    # 原程序结构为：给定 n, m 和长度为 n 的列表 l，然后统计前 m 个元素
    # 这里保持 n = m，并令“原始 n”也等于 n，便于规模控制
    orig_n = n
    m = n

    # 构造确定性的列表 l，长度为 orig_n
    # 使所有元素互不相同，从而触发核心逻辑路径
    # l 中第 i 个元素为 i+1
    l = [i + 1 for i in range(orig_n)]

    d = dict()
    if len(set(l)) < orig_n:
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
    # 示例调用，可自行调整 n 观察规模变化
    main(10)