def main(n):
    # 映射规则：原输入为两个整数 n, k
    # 这里将原始 n 固定为 n，k 由 n 确定性生成
    # 例如：k = n * (n + 1) // 4，确保随 n 增长
    orig_n = n if n > 0 else 1
    k = orig_n * (orig_n + 1) // 4

    cand = 0
    tot = 0
    p = 0
    while tot < k or tot - (orig_n - p) != k:
        cand += 1
        tot += cand
        p += 1

    # print(tot - k)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的值进行实验
    main(10)