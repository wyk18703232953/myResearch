import random

def main(n):
    # 生成规模参数
    # n: 行数
    # 随机生成 m, k，并构造权值图
    m = max(1, n)  # 保证至少为 1 列
    # 生成一个适中的偶数 k，路径长度为 2 * steps
    steps = max(1, n)  # 可根据需要调整规模关联
    k = 2 * steps

    # 随机生成边权，范围可调
    max_w = 10
    # 水平边权: n 行，每行 m-1 个
    hori = [[random.randint(1, max_w) for _ in range(m - 1)] for _ in range(n)]
    # 垂直边权: n-1 行，每行 m 个
    vert = [[random.randint(1, max_w) for _ in range(m)] for _ in range(n - 1)]

    dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    w = [[[0 for _ in range(4)] for _ in range(m)] for _ in range(n)]

    # 填充水平边权
    for i in range(n):
        row = hori[i] if m > 1 else []
        for j in range(m - 1):
            w[i][j + 1][2] = row[j]
            w[i][j][3] = row[j]

    # 填充垂直边权
    for i in range(n - 1):
        row = vert[i]
        for j in range(m):
            w[i][j][1] = row[j]
            w[i + 1][j][0] = row[j]

    # 若 k 为奇数，无法往返
    if k % 2 == 1:
        for _ in range(n):
            print(" ".join(["-1"] * m))
        return
    else:
        k //= 2

    INF = int(40 * 1e6)
    dp = [[[INF for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            dp[i][j][0] = 0

    for d in range(1, k + 1):
        for i in range(n):
            for j in range(m):
                for di, (dx, dy) in enumerate(dxy):
                    ii = i + dx
                    jj = j + dy
                    if 0 <= ii < n and 0 <= jj < m:
                        val = dp[ii][jj][d - 1] + w[i][j][di]
                        if val < dp[i][j][d]:
                            dp[i][j][d] = val

    for i in range(n):
        row_ans = []
        for j in range(m):
            row_ans.append(str(dp[i][j][k] * 2))
        print(" ".join(row_ans))


# 示例调用：可根据需要修改或在外部调用 main(n)
if __name__ == "__main__":
    main(4)