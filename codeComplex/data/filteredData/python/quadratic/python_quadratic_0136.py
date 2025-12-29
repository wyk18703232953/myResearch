from itertools import permutations
import random

def main(n):
    # 1. 生成测试数据：随机生成 4 个 n×n 的 01 矩阵（以字符串形式）
    A = []
    for _ in range(4):
        tmp = []
        for _ in range(n):
            row = ''.join(random.choice('01') for _ in range(n))
            tmp.append(row)
        A.append(tmp)

    # 2. 原逻辑：对 4 个矩阵做排列拼接并计算最小代价
    P = permutations([i for i in range(4)])
    plus = [(0, 0), (0, n), (n, 0), (n, n)]

    tmp = [[0 for _ in range(2 * n)] for _ in range(2 * n)]
    res = 10 ** 17
    for p in P:
        for k in range(4):
            x, y = plus[p[k]]
            for i in range(n):
                for j in range(n):
                    tmp[i + x][j + y] = int(A[k][i][j])

        ans_1 = 0
        ans_2 = 0
        for i in range(2 * n):
            for j in range(2 * n):
                if tmp[i][j] == (i + j) % 2:
                    ans_1 += 1
                else:
                    ans_2 += 1

        res = min(res, ans_1, ans_2)

    print(res)
    return res

if __name__ == "__main__":
    # 示例：n = 3
    main(3)