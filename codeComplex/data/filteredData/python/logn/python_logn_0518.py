def main(n: int):
    N = n
    beg = 0
    end = 9
    i = 0  # в скольки значных числах мы находимся - 1

    while N > end:
        i += 1
        beg, end = end, end + (i + 1) * 9 * 10**i

    n_rel = N - beg - 1  # это N относительно начала чисел с длинной i, начиная с 0
    lvl = i - n_rel % (i + 1)  # номер символа, начиная от конца числа
    period = (i + 1) * 10**lvl  # период смены числа

    res = n_rel // period % 10
    if lvl == i:
        res += 1
    # print(res)
    pass
if __name__ == "__main__":
    # 示例：根据规模 n 自动生成测试数据，这里直接用 n 本身作为输入
    # 可以根据需要改为其他生成方式
    test_n = 100  # 示例规模
    main(test_n)