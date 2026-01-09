def main(n):
    # 数据规模设计：
    # a：序列长度
    # b：查询个数
    # A：长度为 a 的整数序列，确定性生成
    # 约定：a = max(2, n)，b = max(1, n)
    a = max(2, n)
    b = max(1, n)

    # 生成 A：简单的确定性序列
    # A[i] = (i % (n + 1)) + 1，保证正数、可变化
    A = [(i % (n + 1)) + 1 for i in range(a)]

    A.append(-1)
    B = []
    Z = []
    AN = []
    x, y = A[0], A[1]

    for i in range(a - 1):
        Z.append((x, y))
        if x > y:
            B.append(y)
            y = A[i + 2]

        else:
            B.append(x)
            x, y = y, A[i + 2]

    # 生成 b 个查询 w，原本是从输入读取
    # 这里使用确定性构造：
    # 既包含小于等于 len(Z) 的值，也包含大于 len(Z) 的值
    # w_k = k + 1，当需要大值时加上 len(Z)
    queries = []
    LZ = len(Z)
    for i in range(b):
        if i % 2 == 0:
            # 偶数索引：保证在 1..LZ 范围内（若 LZ>0）
            if LZ > 0:
                w = (i % LZ) + 1

            else:
                w = 1

        else:
            # 奇数索引：构造大一些的数
            if LZ > 0:
                w = LZ + i + 1

            else:
                w = i + 2
        queries.append(w)

    for w in queries:
        if w <= len(Z):
            AN.append(Z[w - 1])

        else:
            if len(B) == 0:
                # 极端情况下 B 为空，避免除以零，构造一个固定对
                AN.append((x, x))

            else:
                w = w % len(B)
                AN.append((x, B[w - 1]))

    for W in AN:
        # print(*W)
        pass
if __name__ == "__main__":
    main(10)