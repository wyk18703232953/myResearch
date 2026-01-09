def main(n):
    # 映射含义：
    # 原程序有 4 个整数输入：n, m, a, b
    # 这里将参数 n 作为“输入规模”，用来确定 m, a, b 的大小范围
    # 原始 n 的值用 n_self 表示
    n_self = n

    # 为避免除零，m 至少为 1
    # 让 m 随规模线性增长，但不超过 n_self 且至少为 1
    m = max(1, n_self // 2 + 1)

    # 构造 a, b 与规模相关，且为正整数
    a = n_self + 3
    b = max(1, n_self // 3 + 2)

    if n_self % m != 0:
        mn = n_self // m * m
        mx = n_self // m * m + m
        result = min(((n_self - mn) * b), ((mx - n_self) * a))

    else:
        result = 0

    # print(result)
    pass
if __name__ == "__main__":
    main(10)