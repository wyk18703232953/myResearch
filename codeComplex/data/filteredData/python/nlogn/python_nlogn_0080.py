def main(n):
    # 确定性构造 x
    x = (n // 2) + 1
    if x > n:
        x = n

    # 构造 n 行 (p, q)，p 有重复以保证统计有意义
    a = []
    k = {}
    for i in range(1, n + 1):
        p = i // 2  # 制造重复的 p
        q = i       # 任意确定性 q
        if p not in k:
            k[p] = 1
        a.append([p, q])

    a.sort()
    k_sorted = sorted(k)
    k_sorted = k_sorted[::-1]

    p_list = []
    for key in k_sorted:
        for j in a:
            if j[0] == key:
                p_list.append(j)

    # 保证下标安全
    if 1 <= x <= len(p_list):
        result = p_list.count(p_list[x - 1])

    else:
        result = 0

    # print(result)
    pass
if __name__ == "__main__":
    main(10)