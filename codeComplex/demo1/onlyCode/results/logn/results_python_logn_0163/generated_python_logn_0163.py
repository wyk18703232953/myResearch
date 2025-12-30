def main(n: int):
    """
    将原程序改为函数形式：
    - n 作为规模，生成测试数据 N, K
    - 此处示例选择：N = n，K = n（可按需要自行调整生成规则）
    """

    N = n
    K = n

    def in_bounds(k: int) -> bool:
        return N <= K * (K + 1) // 2 - (K - k) * (K - k + 1) // 2 - k + 1

    l = 0
    r = K
    while l <= r:
        c = (l + r) // 2
        if in_bounds(c):
            r = c - 1
        else:
            l = c + 1

    if in_bounds(K):
        print(l)
    else:
        print(-1)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)