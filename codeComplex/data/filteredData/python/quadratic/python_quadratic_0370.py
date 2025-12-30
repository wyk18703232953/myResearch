import random
from itertools import accumulate

def main(n):
    # 生成测试数据：随机生成一个 n 行 n 列、包含 '.' 和 '*' 的网格
    m = n
    # 保证既有 '*' 也有 '.'，方便测试
    S = []
    for i in range(n):
        row = []
        for j in range(m):
            # 约一半概率为 '*'
            row.append('*' if random.random() < 0.5 else '.')
        S.append(row)

    L = [[0] * m for _ in range(n)]
    R = [[0] * m for _ in range(n)]
    U = [[0] * m for _ in range(n)]
    D = [[0] * m for _ in range(n)]

    # 预处理左右方向连续 '*' 数量
    for i in range(n):
        cnt = 0
        for j in range(m):
            if S[i][j] == '.':
                cnt = 0
            else:
                cnt += 1
                L[i][j] = cnt
        cnt = 0
        for j in reversed(range(m)):
            if S[i][j] == '.':
                cnt = 0
            else:
                cnt += 1
                R[i][j] = cnt

    # 预处理上下方向连续 '*' 数量
    for j in range(m):
        cnt = 0
        for i in range(n):
            if S[i][j] == '.':
                cnt = 0
            else:
                cnt += 1
                U[i][j] = cnt
        cnt = 0
        for i in reversed(range(n)):
            if S[i][j] == '.':
                cnt = 0
            else:
                cnt += 1
                D[i][j] = cnt

    imosH = [[0] * (m + 1) for _ in range(n)]
    imosV = [[0] * m for _ in range(n + 1)]
    ans = []

    # 找所有十字中心及臂长
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if S[i][j] == '.':
                continue
            l = L[i][j] - 1
            r = R[i][j] - 1
            u = U[i][j] - 1
            d = D[i][j] - 1
            s = min(l, r, u, d)
            if s == 0:
                continue
            ans.append((i + 1, j + 1, s))
            imosV[i - s][j] += 1
            imosV[i + s + 1][j] -= 1
            imosH[i][j - s] += 1
            imosH[i][j + s + 1] -= 1

    # 累加得到覆盖次数
    for i in range(n):
        imosH[i] = list(accumulate(imosH[i]))
    for j in range(m):
        for i in range(1, n + 1):
            imosV[i][j] += imosV[i - 1][j]

    # 校验是否所有 '*' 都被十字覆盖
    for i in range(n):
        for j in range(m):
            if S[i][j] == '*':
                if imosH[i][j] <= 0 and imosV[i][j] <= 0:
                    print(-1)
                    return

    print(len(ans))
    for x, y, s in ans:
        print(x, y, s)