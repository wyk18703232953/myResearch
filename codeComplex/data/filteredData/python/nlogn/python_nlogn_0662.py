import random

def main(n):
    mod = 998244353

    # 生成测试数据：长度为 n 的排列，部分位置替换为 -1
    # 基本思路：从 1..n 的排列中随机挑一些位置置为 -1，保证非 -1 元素互不相同
    vals = list(range(1, n + 1))
    random.shuffle(vals)
    P = vals[:]  # 先当作完整排列

    # 随机决定空缺数量（0..n）
    BLA = random.randint(0, n)
    # 随机选择 BLA 个下标置 -1
    if BLA > 0:
        idxs = random.sample(range(n), BLA)
        for i in idxs:
            P[i] = -1

    INV = [None] * (n + 1)  # 1/a 的列表
    for i in range(1, n + 1):
        INV[i] = pow(i, mod - 2, mod)

    BLA = P.count(-1)

    if BLA == 0 or BLA == 1:
        ANS = 0
    else:
        LEFT = BLA * (BLA - 1) // 2 * INV[BLA] % mod  # 左側の個数の平均
        AVEP = BLA * (BLA - 1) // 2 * pow(BLA - 1, mod - 2, mod) % mod  # 左側にあるものが自分より大きい確率の和
        ANS = LEFT * AVEP % mod

    y = 1
    for i in range(BLA):
        y = y * (BLA - i) % mod

    KOSUU = pow(y, mod - 2, mod)  # 未使用变量，保留以保持结构一致

    BLALIST = [1] * (n + 1)
    NONBLA = []
    BLANUM = [0] * n
    for i in range(n):
        if P[i] != -1:
            BLALIST[P[i]] = 0
            BLANUM[i] = BLANUM[i - 1]
            NONBLA.append(P[i])
        else:
            BLANUM[i] = BLANUM[i - 1] + 1

    BLALIST[0] = 0
    for i in range(1, n + 1):
        BLALIST[i] = BLALIST[i - 1] + BLALIST[i]

    if BLA != 0:
        for i in range(n):
            if P[i] != -1:
                ANS = (
                    ANS
                    + (
                        BLANUM[i] * (BLA - BLALIST[P[i]])
                        + (BLA - BLANUM[i]) * BLALIST[P[i]]
                    )
                    * INV[BLA]
                ) % mod

    A = NONBLA

    if A == []:
        print(ANS)
        return

    nA = len(A)
    MAXA = max(A)
    MINA = min(A)

    BIT = [0] * (MAXA - MINA + 2)  # 出現回数をbit indexed treeの形でもっておく.

    for i in range(nA):  # A[0],A[1],...とBITを更新
        bitobje = A[i] - MINA + 1

        x = bitobje
        while x != 0:
            ANS = (ANS - BIT[x]) % mod
            x -= (x & -x)

        x2 = MAXA - MINA + 1
        while x2 != 0:
            ANS = (ANS + BIT[x2]) % mod
            x2 -= (x2 & -x2)

        y = bitobje
        while y <= MAXA - MINA + 1:
            BIT[y] += 1
            y += (y & -y)

    print(ANS)


if __name__ == "__main__":
    # 举例：调用 main(5)
    main(5)