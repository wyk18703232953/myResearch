def main(n):
    # 解释输入结构：
    # 原程序需要四个整数 n, m, k, l
    # 此处将参数 n 作为“输入规模”，并据此构造这四个数：
    #   N = 4 * n
    #   M = 2 * n + 1
    #   K = n
    #   L = n // 2
    # 这些构造是确定性的且随 n 线性增长。
    N = 4 * n
    M = 2 * n + 1
    K = n
    L = n // 2

    if K + L > N:
        # print(-1)
        pass

    else:
        x = (K + L) // M + (1 if (K + L) % M != 0 else 0)
        if x * M > N:
            # print(-1)
            pass

        else:
            # print(x)
            pass
if __name__ == "__main__":
    # 示例：以 n = 10 作为规模进行一次调用
    main(10)