import random

def main(n):
    # 1. 生成测试数据：4 个 n×n 的 01 矩阵（用字符串表示）
    # 原程序中是逐行读入字符串，这里随机生成
    s = [["" for _ in range(n)] for __ in range(4)]
    for i in range(4):
        for j in range(n):
            # 生成长度为 n 的随机 01 串
            s[i][j] = ''.join(random.choice('01') for _ in range(n))

    # 2. 按原逻辑枚举 4 个象限的排列，构造 2n×2n 的棋盘并计算修改代价
    res = int(1e13)
    for i in range(24):  # 4! = 24
        perm = [0, 1, 2, 3]
        L = [0] * 4
        tmp = i
        # Lehmer 编码生成排列
        for j in range(4):
            L[j] = tmp % (4 - j)
            tmp //= (4 - j)
        LL = [0] * 4
        for j in range(4):
            LL[j] = perm[L[j]]
            for k in range(L[j], 3 - j):
                perm[k] = perm[k + 1]

        lu, ru, ld, rd = LL[0], LL[1], LL[2], LL[3]

        # 拼成 2n×2n 的棋盘
        Map = [s[lu][_][:] + s[ru][_][:] for _ in range(n)] + \
              [s[ld][_][:] + s[rd][_][:] for _ in range(n)]

        cnt0, cnt1 = 0, 0
        # 计算两种起点方案的最小修改次数
        for j in range(2 * n):
            for k in range(2 * n):
                if (j + k) % 2:
                    if Map[j][k] == '0':
                        cnt0 += 1
                    else:
                        cnt1 += 1
                else:
                    if Map[j][k] == '1':
                        cnt0 += 1
                    else:
                        cnt1 += 1
        res = min(res, cnt0, cnt1)

    print(res)


if __name__ == "__main__":
    # 示例：规模 n=3
    main(3)