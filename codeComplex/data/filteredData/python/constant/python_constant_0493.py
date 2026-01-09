def main(n):
    # 原程序输入结构：两个整数 n_input, k_input
    # 将实验规模参数 n 作为原程序的 n_input
    n_input = max(1, n)
    # 构造确定性的 k_input，与 n_input 线性相关
    k_input = 3 * n_input + 5

    q = 2 * n_input + 1
    p = k_input // n_input
    if k_input % n_input:
        result = p + 1

    else:
        result = p
    # print(result)
    pass
if __name__ == "__main__":
    main(10)