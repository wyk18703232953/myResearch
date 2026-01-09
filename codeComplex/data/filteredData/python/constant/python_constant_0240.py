def main(n):
    # 根据原始程序输入结构：
    # 第一个 input() -> n
    # 第二个 input() -> m
    # 这里将规模参数 n 映射为原代码中的 n
    # 并确定性构造 m
    original_n = n
    m = n * n + 3 * n + 7

    if original_n <= 26:
        result = m % (2 ** original_n)

    else:
        result = m

    # print(result)
    pass
if __name__ == "__main__":
    main(10)