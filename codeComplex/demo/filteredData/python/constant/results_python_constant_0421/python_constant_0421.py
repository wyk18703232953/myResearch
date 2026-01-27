def main(n):
    # 将 n 映射为 (N, K)，构造确定性输入规模
    # 这里设定 N = n，K = n//2 + 1，保证随 n 线性增长
    N = max(1, n)
    K = n // 2 + 1

    # 原算法逻辑
    if 2 * N - 1 < K:
        result = 0
    elif K <= N + 1:
        if K % 2:
            result = K // 2

        else:
            result = K // 2 - 1

    else:
        t1 = K - N
        if K % 2 == 0:
            result = K // 2 - t1

        else:
            result = K // 2 - t1 + 1

    # print(result)
    pass
if __name__ == "__main__":
    main(10)