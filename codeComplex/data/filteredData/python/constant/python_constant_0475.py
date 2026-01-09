def main(n):
    # 原程序期望的输入结构是两个整数 N, K
    # 在这里我们将 n 解释为 N，而 K 由 N 和 n 确定性构造
    N = max(1, n)
    K = N * N + N  # 确定性构造，且随 n 增长

    result = (K + N - 1) // N
    # print(result)
    pass
if __name__ == "__main__":
    main(10)