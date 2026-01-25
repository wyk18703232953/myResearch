def main(n):
    # 映射规则：
    # n >= 2 时：
    #   第一个输入行: "n c" 其中 n_len = n, c = n // 2
    #   第二个输入行: n_len 个整数 ai，取值范围 [0, 500000]
    # 数据构造为确定性的：ai = (i * 123457) % 500001
    if n < 2:
        # 对于过小的 n，退化为最小有意义规模
        n_len = 2
    else:
        n_len = n
    c = n_len // 2
    res1 = [0] * 500001
    res = 0
    # 构造与原程序第二行输入等价的数据序列
    for i in range(n_len):
        ai = (i * 123457) % 500001
        res1[ai] = max(res1[ai], res1[c])
        res1[ai] += 1
        res = max(res, res1[ai] - res1[c])
    print(res + res1[c])


if __name__ == "__main__":
    # 示例调用，可根据需要调整 n 的规模
    main(10)