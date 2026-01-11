def main(n):
    # 根据原程序结构生成确定性输入：
    # n: 作为 h 列表的长度
    if n < 2:
        n = 2

    # 生成 nab: [n, a, b]
    # a 在原程序中未实际使用，这里设为 0
    a = 0
    b = n // 2  # 保证 0 <= b < n
    nab = [n, a, b]

    # 生成 h：确定性递增序列，保证排序后有序且有差值
    h = [i * 2 for i in range(n)]
    h_sorted = sorted(h)

    # 保持原程序核心逻辑：输出 h[b] - h[b-1]
    # 但需防止 b 为 0 的情况（原代码中 b-1 会变为 -1）
    if nab[2] <= 0:
        # 若 b <= 0，则调整为 1，避免负索引影响实验
        b_index = 1
    elif nab[2] >= n:
        # 若 b 越界，则调整为最后一个合法位置
        b_index = n - 1

    else:
        b_index = nab[2]

    result = h_sorted[b_index] - h_sorted[b_index - 1]
    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要调整 n 的规模
    main(10)