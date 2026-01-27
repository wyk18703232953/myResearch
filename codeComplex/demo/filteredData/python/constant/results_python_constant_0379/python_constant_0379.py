def main(n):
    # 原程序需要 a, b, c, n 四个整数作为输入
    # 这里将 n 解释为输入规模，用确定性方式生成 a, b, c, N_real
    # 保持与原程序同样的变量含义：a, b, c, n(这里用 N_real 表示)
    a = n
    b = 2 * n
    c = n // 2
    N_real = 3 * n + 1  # 实际参与算法的 n

    p = (a + b - c)
    f = N_real - p
    if p >= N_real or c > a or c > b:
        # print("-1")
        pass

    else:
        # print(f)
        pass
if __name__ == "__main__":
    main(10)