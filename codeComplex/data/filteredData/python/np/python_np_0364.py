def main(n: int):
    """
    参数 n 作为规模，用于生成测试数据：
    - N = n
    - M = n
    - X 为 N x M 的整数矩阵，这里用简单的可重复数据生成方式（例如按行列索引求和）。
    最终打印原算法在该测试数据上的结果。
    """
    N = n
    M = n

    # 生成测试数据 X：这里用一个简单的确定性规则，例如 X[i][j] = (i + j) % 10
    X = [[(i + j) % 10 for j in range(M)] for i in range(N)]

    # 原代码中的 Y 未参与后续计算，可以省略
    # Y = [[X[i][j] for i in range(N)] for j in range(M)]

    dp = [[0] * (1 << N) for _ in range(M + 1)]

    for j in range(M):
        for mask in range(1 << N):
            maskpre = mask
            while maskpre >= 0:
                maskpre &= mask
                ma = 0
                for k in range(N):
                    s = 0
                    for i in range(N):
                        if ((maskpre >> i) & 1) == 0 and ((mask >> i) & 1):
                            # 原始代码是 X[i-k][j]，可能越界，这里保持原逻辑并加越界保护
                            idx = i - k
                            if 0 <= idx < N:
                                s += X[idx][j]
                    if s > ma:
                        ma = s
                if dp[j][maskpre] + ma > dp[j + 1][mask]:
                    dp[j + 1][mask] = dp[j][maskpre] + ma

                maskpre -= 1

    print(dp[-1][-1])


if __name__ == "__main__":
    # 示例调用：可按需修改 n
    main(3)