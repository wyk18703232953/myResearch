def main(n):
    # 根据原始程序的输入结构，原来是读取两个整数 n, k
    # 这里将 n 作为“输入规模”，并构造确定性的 (n, k)
    # 为保证 n >= 1，避免除零
    if n <= 0:
        n_val = 1

    else:
        n_val = n
    # 构造一个与规模线性相关的 k
    # 保证确定性：同一 n 得到同一 k
    k_val = n_val * n_val + 3 * n_val + 1

    result = (k_val + n_val - 1) // n_val
    # print(result)
    pass
if __name__ == "__main__":
    main(10)