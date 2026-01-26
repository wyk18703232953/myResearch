def main(n):
    # 解释输入结构：
    # 原程序有两行：
    # 1) n, m
    # 2) 一个长度为 n 的字符串序列 seq
    # 3) 一个长度为 m 的字符串序列 fp
    #
    # 这里新的 main(n) 只保留一个参数 n，
    # 我们将原来的 n, m 都映射为 n，以保证规模含义清晰：
    #   len(seq) = n
    #   len(fp)  = n
    #
    # 数据构造保持完全确定性：
    #   seq = ["s0", "s1", ..., "s(n-1)"]
    #   fp  = ["s(i)" 其中 i 为 0 到 n-1 中所有偶数]
    #
    # 这样 checklist 等价于 seq 中那些也出现在 fp 的元素
    # 即所有偶数下标的 "s{i}"。
    if n < 0:
        raise ValueError("n must be non-negative")

    # 构造 seq 和 fp
    seq = ["s{}".format(i) for i in range(n)]
    fp = ["s{}".format(i) for i in range(0, n, 2)]

    # 保持原核心算法逻辑
    checklist = []
    for number in seq:
        if number in fp:
            checklist.append(number)

    # print(" ".join(checklist))
    pass
if __name__ == "__main__":
    # 示例调用，可按需修改 n 的大小做时间复杂度实验
    main(10)