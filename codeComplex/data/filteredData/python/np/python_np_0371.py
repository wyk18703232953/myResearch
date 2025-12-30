import random


def main(n: int):
    # 生成测试数据：
    # n 作为 N，M 也设为 n
    N = n
    M = n
    # 生成 N×M 的矩阵 X，元素为小整数，便于调试
    # 可根据需要调整数据范围
    X = [[random.randint(-5, 5) for _ in range(M)] for _ in range(N)]

    # 原代码中生成的 Y 实际未使用，这里可省略
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
                            # 注意：原代码 X[i-k][j] 这里会在 i<k 时下标为负，
                            # Python 支持负索引，保持行为一致
                            s += X[i - k][j]
                    if s > ma:
                        ma = s
                if dp[j][maskpre] + ma > dp[j + 1][mask]:
                    dp[j + 1][mask] = dp[j][maskpre] + ma

                maskpre -= 1

    # 输出与原逻辑等价的结果
    print(dp[-1][-1])


if __name__ == "__main__":
    # 示例：调用 main，规模为 3
    main(3)