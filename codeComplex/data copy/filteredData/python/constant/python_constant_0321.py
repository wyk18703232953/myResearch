def main(n: int):
    """
    n: 规模，即数组 A 的长度。
    测试数据生成规则：A[i] = i + 1
    """
    # 生成测试数据
    A = [i + 1 for i in range(n)]
    N = len(A)

    dp = [0] * N
    for i in range(N):
        B = A.copy()
        each = B[i] // N
        curr = B[i]
        B[i] = 0
        for j in range(N):
            B[j] += each
        for j in range(1, (curr - each * N) + 1):
            B[(i + j) % N] += 1
        for M in B:
            if M % 2 == 0:
                dp[i] += M
    ans = max(dp)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)