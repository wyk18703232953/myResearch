import sys
import random

# 原始逻辑封装为 main(n)
def main(n):
    # 生成规模为 n 的测试数据
    # 自由设定 m 的规模，这里取 m = max(2, n) 作为示例
    m = max(2, n)

    # 生成测试矩阵 MAT，保证整数、可控范围
    # 这里生成递增序列叠加少量随机性，便于调试
    random.seed(0)
    MAT = []
    base = 0
    for i in range(n):
        row = []
        cur = base
        for j in range(m):
            cur += random.randint(0, 10)
            row.append(cur)
        MAT.append(row)
        base += 5  # 不同行稍微错开

    # 下面是原程序逻辑（去除 input()、直接使用生成的 MAT, n, m）

    if n == 1:
        ANS = 10 ** 10
        for i in range(1, m):
            if ANS > abs(MAT[0][i] - MAT[0][i - 1]):
                ANS = abs(MAT[0][i] - MAT[0][i - 1])
        print(ANS)
        return

    EDGE0 = [[10 ** 10] * n for _ in range(n)]  # i が 0 行目, j が最終行
    EDGE1 = [[10 ** 10] * n for _ in range(n)]
    MAX = 0
    MIN = 0

    if m != 1:
        for i in range(n):
            for j in range(n):
                EDGE1[i][j] = EDGE1[j][i] = min(
                    abs(MAT[i][k] - MAT[j][k]) for k in range(m)
                )
                if EDGE1[i][j] > MAX:
                    MAX = EDGE1[i][j]
                EDGE0[i][j] = min(
                    abs(MAT[i][k] - MAT[j][k - 1]) for k in range(1, m)
                )
    else:
        for i in range(n):
            for j in range(n):
                EDGE1[i][j] = EDGE1[j][i] = min(
                    abs(MAT[i][k] - MAT[j][k]) for k in range(m)
                )
                if EDGE1[i][j] > MAX:
                    MAX = EDGE1[i][j]

    # Hamilton 関数内で参照するため、外側の変数を nonlocal 的に閉包
    def Hamilton(start, USED, rest, last, weight, MEMO):
        if MEMO[last * (1 << n) + USED] != 2:
            return MEMO[last * (1 << n) + USED]
        if rest == 1:
            for i in range(n):
                if USED & (1 << i) == 0:
                    final = i
                    break

            if EDGE0[start][final] >= weight and EDGE1[last][final] >= weight:
                MEMO[last * (1 << n) + USED] = 1
                return 1
            else:
                MEMO[last * (1 << n) + USED] = 0
                return 0

        for j in range(n):
            if (USED & (1 << j) == 0) and EDGE1[last][j] >= weight:
                NEXT = USED + (1 << j)
                if Hamilton(start, NEXT, rest - 1, j, weight, MEMO) == 1:
                    MEMO[last * (1 << n) + USED] = 1
                    return 1
        else:
            MEMO[last * (1 << n) + USED] = 0
            return 0

    while MAX != MIN:
        aveweight = (MAX + MIN + 1) // 2

        for start in range(n):
            MEMO = [2] * (n * (1 << (n + 1)))
            START = 1 << start
            if Hamilton(start, START, n - 1, start, aveweight, MEMO) == 1:
                MIN = aveweight
                break
        else:
            MAX = aveweight - 1

    print(MAX)


# 示例调用：如果作为脚本运行，可以在此处指定 n
if __name__ == "__main__":
    # 例如用 n = 5 进行测试
    main(5)