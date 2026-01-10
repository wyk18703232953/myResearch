def main(n):
    # 生成确定性的度数组结构：
    # n >= 3: 构造一个度数数组 a，满足：
    # - 至少一个度数为 1（leaf）
    # - 至少两个度数 > 1（other）
    # - sum(a) 为偶数且 >= 2*(n-1)，保证可以构造连通图
    # 构造方案：
    # - 当 n < 3 时，直接打印 NO，与原算法逻辑保持一致（其假设 n >= 3）
    # - 对于 n >= 3：
    #   * a[0] = 1（leaf）
    #   * 对 i=1 到 n-2: a[i] = 2 + (i % 3)
    #   * a[n-1] = 2
    #   该构造确保存在多个 other，并且叶子数量至少 1

    if n < 3:
        print("NO")
        return

    a = [0] * n
    if n == 3:
        # 特殊小规模：1,2,2
        a[0] = 1
        a[1] = 2
        a[2] = 2
    else:
        a[0] = 1
        for i in range(1, n - 1):
            a[i] = 2 + (i % 3)
        a[n - 1] = 2

    leafs = set()
    other = {}
    other_indices = []
    s = 0
    for i, val in enumerate(a):
        if val == 1:
            leafs.add(i)
        else:
            other[i] = val
            other_indices.append(i)
        s += val

    if not other:
        # n >= 3，但所有度数都是 1，则输出 NO
        print("NO")
        return

    other_indices.sort(key=lambda index: other[index])
    other_indices = [other_indices[-1]] + other_indices[:-1]

    edges = []
    for i1, i2 in zip(other_indices, other_indices[1:]):
        edges.append((i1, i2))
        other[i1] -= 1
        if other[i1] == 0:
            del other[i1]
        other[i2] -= 1
        if other[i2] == 0:
            del other[i2]

    diam = len(other_indices) + min(2, len(leafs))

    has_start = has_end = False

    while leafs:
        if len(other) == 0:
            print("NO")
            return
        l = leafs.pop()
        if not has_start and other.get(other_indices[0], 0):
            i = other_indices[0]
            has_start = True
        elif not has_end and other.get(other_indices[-1], 0):
            i = other_indices[-1]
            has_end = True
        else:
            i = next(iter(other))
        edges.append((l, i))
        other[i] -= 1
        if other[i] == 0:
            del other[i]

    print("YES", diam - 1)
    print(len(edges))
    for x, y in edges:
        print(x + 1, y + 1)


if __name__ == "__main__":
    # 示例：使用 n = 10 作为输入规模
    main(10)