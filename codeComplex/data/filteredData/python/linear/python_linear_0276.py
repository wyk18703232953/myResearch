def main(n):
    # 将参数 n 拆分成原程序需要的 n, m, a, b，保持确定性
    # 约束：m >= 1，a,b >= 1
    if n < 4:
        # 对于非常小的 n，给一个固定可行的参数组合
        N = 1
        M = 1
        A = 1
        B = 1
    else:
        N = n
        M = max(1, n // 2)
        A = (n % 7) + 1
        B = (n % 5) + 1

    if N < M:
        result = min(A * (M - N), B * N)
    else:
        result = min(B * (N % M), A * (M - (N % M)))
    print(result)


if __name__ == "__main__":
    main(10)