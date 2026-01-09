def main(n):
    # 将 n 映射为原程序中的 n, m, a, b
    # 保证 m > 0，且规模随 n 线性增长，保持确定性
    N = n
    M = n + 1
    A = n + 2
    B = n + 3

    if N < M:
        result = min(A * (M - N), B * N)

    else:
        result = min(B * (N % M), A * (M - (N % M)))
    # print(result)
    pass
if __name__ == "__main__":
    main(10)