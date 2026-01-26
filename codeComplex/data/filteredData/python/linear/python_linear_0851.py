def main(n):
    if n <= 0:
        return
    # 构造长度为 n 的整数列表 l：
    # 先严格递增到某个峰值，再严格递减，保持原算法逻辑有意义
    peak = n // 2
    l = [i for i in range(peak)] + [peak] + [peak - (i - peak - 1) - 1 for i in range(peak + 1, n)]
    to = l.index(max(l))
    ok = 1
    for i in range(1, to):
        if l[i] <= l[i - 1]:
            ok = 0
            break
    for i in range(to + 1, n):
        if l[i] >= l[i - 1]:
            ok = 0
            break
    if ok:
        # print('YES')
        pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    main(10)