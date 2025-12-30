from math import inf
import random

def main(n):
    # 生成规模参数
    # n: 行数
    # 为了保持原程序语义，再生成 m, k
    m = n                 # 列数，这里设为 n，可按需修改
    k = 2 * random.randint(1, 5)  # 保证 k 为偶数且不太大，便于测试

    # 生成测试数据：cosp 为 n x (m+1)，最后一列为 inf
    cosp = [[random.randint(1, 10) for _ in range(m)] + [inf] for _ in range(n)]
    # cosv 为 (n-1) x m，加一行 inf
    cosv = [[random.randint(1, 10) for _ in range(m)] for _ in range(n - 1)] + [[inf] * m]

    # 按原逻辑计算
    if k % 2 == 1:
        for _ in range(n):
            print(*[-1] * m)
    else:
        dp = [[0] * m for _ in range(n)]
        xx, yy = [0, 0, 1, -1], [1, -1, 0, 0]

        for _ in range(k // 2):
            dp1 = [[inf] * m for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    for kk in range(4):
                        x1, y1 = i + xx[kk], j + yy[kk]
                        # 边界检查（原代码缺失，合理补全）
                        if not (0 <= x1 < n and 0 <= y1 < m):
                            continue
                        if kk < 2:
                            if kk == 1:
                                if j - 1 < 0:
                                    continue
                                edge = cosp[i][j - 1]
                            else:
                                edge = cosp[i][j]
                        else:
                            if kk == 3:
                                if i - 1 < 0:
                                    continue
                                edge = cosv[i - 1][j]
                            else:
                                edge = cosv[i][j]
                        if edge != inf:
                            dp1[i][j] = min(dp1[i][j], 2 * edge + dp[x1][y1])
            dp = [row[:] for row in dp1]

        for row in dp:
            print(*row)

if __name__ == "__main__":
    main(4)