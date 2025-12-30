import random

def main(n):
    # 生成测试数据
    # n: X 的规模
    # m: Y 的规模，这里取与 n 同级（可按需要调整）
    m = n

    # X: 随机生成 1 ~ 1e9 的整数
    X = [random.randint(1, 10**9) for _ in range(n)]

    Y = []
    for _ in range(m):
        t = random.randint(1, 2)
        if t == 1:
            # 生成若干 (1, v) 类型，其中有概率生成 (1, 1e9)
            if random.random() < 0.2:
                v = 10**9
            else:
                v = random.randint(1, 10**9)
        else:
            # 也允许出现非 1 类型的 y[0]，根据原逻辑会被忽略
            v = random.randint(1, 10**9)
        Y.append([t, v])

    # 原始逻辑
    Z = []
    ANS = 0
    for y in Y:
        if y[0] == 1 and y[1] == 10**9:
            ANS += 1
        elif y[0] == 1:
            Z.append(y[1])

    X.sort(reverse=True)
    Z.sort(reverse=True)

    XCOUNT = [0] * n  # X[i] より大きい Z の個数

    i = 0
    j = 0
    l = len(Z)
    X.append(0)
    Z.append(0)
    while i < l + 1 and j < n:
        if Z[i] >= X[j]:
            i += 1
        else:
            XCOUNT[j] = i
            j += 1

    count = n
    XCOUNT.reverse()
    for i in range(n):
        if count > i + XCOUNT[i]:
            count = i + XCOUNT[i]

    print(count + ANS)


if __name__ == "__main__":
    # 示例：运行 main(10)
    main(10)