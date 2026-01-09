def main(n):
    # 根据 n 构造确定性输入规模
    # 原程序需要 n 和 s，这里的 n 作为规模参数，
    # 实际计算中使用:
    #   n_input = n + 1  (避免除零)
    #   s_input = n * (n + 1)
    n_input = n + 1
    s_input = n * (n + 1)

    big = s_input // n_input
    r = s_input - big * n_input
    if r > 0:
        result = big + 1

    else:
        result = big

    # print(result)
    pass
if __name__ == "__main__":
    main(10)