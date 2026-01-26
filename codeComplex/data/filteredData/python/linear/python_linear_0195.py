def main(n):
    # 映射含义：
    # n: 列表长度
    #
    # 生成确定性输入：
    # a, b, c, t 为确定性常数（可根据需要调整，但与 n 无关以便对比）
    a = 2
    b = 1
    c = 3
    t = 5 + n  # 让 t 随规模线性增大，方便时间复杂度实验

    # l 为长度为 n 的整数列表，完全由 n 确定性生成
    # 元素既不全相同，又有一定分布，避免退化
    l = [(i * 2) % (t + 3) for i in range(n)]

    if c > b:
        r = 0
        for i in l:
            k = t - i
            k *= (c - b)
            r += k
        # print(a * n + r)
        pass

    else:
        # print(a * n)
        pass
if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)