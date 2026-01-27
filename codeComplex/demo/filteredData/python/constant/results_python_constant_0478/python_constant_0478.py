def main(n):
    # 原程序输入结构：单组两个整数 n, k
    # 在重构中：第一个参数 n 作为“输入规模”，用于构造一组 (n_value, k_value)
    # 这里令 n_value = max(1, n)，k_value = n * (n + 1) 的确定性构造
    n_value = max(1, n)
    k_value = n_value * (n_value + 1)
    result = (k_value + n_value - 1) // n_value
    # print(result)
    pass
if __name__ == "__main__":
    main(10)