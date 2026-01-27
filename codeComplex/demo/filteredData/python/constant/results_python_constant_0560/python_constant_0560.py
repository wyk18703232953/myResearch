def main(n):
    # 将 n 映射为 N, M, K, L 的确定性构造
    # 确保参数非零且有一定规模变化
    N = max(1, n)
    M = max(1, n // 3 + 1)
    K = max(0, n // 4)
    L = max(0, n // 5)

    if N < M or K + L > N:
        # print(-1)
        pass

    else:
        x = (L + K - 1) // M + 1
        if x * M <= N:
            # print(x)
            pass

        else:
            # print(-1)
            pass
if __name__ == "__main__":
    main(10)