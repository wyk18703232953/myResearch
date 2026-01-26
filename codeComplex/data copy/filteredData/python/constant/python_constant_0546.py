def main(n):
    # 原程序输入结构：两个整数 n, s
    # 这里将输入规模参数 n 映射为：
    #   n_input = n
    #   s_input = n * (n + 1) // 2  （确定性构造，随 n 增长）
    n_input = n if n > 0 else 1
    s_input = n_input * (n_input + 1) // 2
    result = (s_input + n_input - 1) // n_input
    # print(result)
    pass
if __name__ == "__main__":
    main(10)