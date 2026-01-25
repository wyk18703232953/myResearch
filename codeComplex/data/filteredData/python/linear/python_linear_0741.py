def count(audrey, imba, banget):
    return (imba - audrey - 1) % (banget - 1)

def main(n):
    # 约定：n >= 2
    if n < 2:
        n = 2

    # 确定性生成 n, q
    # 使用规模 n 来决定数组长度和查询次数
    array_len = n
    q = n

    # 生成确定性的数组 L，长度为 array_len
    # 简单构造：L[i] = (i * 2 + 3) % (array_len + 5) + 1
    L = [((i * 2 + 3) % (array_len + 5)) + 1 for i in range(array_len)]

    maxi = max(L)
    indexmax = L.index(maxi)
    P = []

    for i in range(indexmax):
        P.append((L[0], L[1]))
        if L[0] < L[1]:
            L.append(L.pop(0))
        else:
            L.append(L.pop(1))

    Y = tuple(L[1:])

    # 生成 q 个确定性查询 m
    # 使用简单算术构造，保证覆盖 m <= indexmax 和 m > indexmax 的情况
    queries = []
    for i in range(q):
        # 先生成一个基本值
        base = i + 1
        if i % 2 == 0:
            # 尝试生成小于等于 indexmax 的 m
            m = (base % (indexmax + 1)) + 1 if indexmax > 0 else 1
        else:
            # 尝试生成大于 indexmax 的 m
            m = base + indexmax + 1
        queries.append(m)

    out_lines = []
    for m in queries:
        if m <= indexmax:
            out_lines.append(f"{P[m-1][0]} {P[m-1][1]}")
        else:
            out_lines.append(f"{maxi} {Y[count(indexmax, m, array_len)]}")

    print("\n".join(out_lines))

if __name__ == "__main__":
    main(10)