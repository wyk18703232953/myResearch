def main(n):
    global a, m
    if n <= 0:
        return
    # 定义列数规模 m，随 n 增长但有上界，保证位运算可控
    m = min(10, max(1, n // 10))
    # 生成一个确定性的 n x m 矩阵 a
    # a[i][j] = i * (j + 1) + (i + j) % 7，保证元素分布有一定变化
    a = [[i * (j + 1) + (i + j) % 7 for j in range(m)] for i in range(n)]

    def check(x: int):
        vis = {}
        for i, array in enumerate(a):
            t = 0
            for j, val in enumerate(array):
                if val >= x:
                    t |= 1 << j
            vis[t] = i
        full = (1 << m) - 1
        if full in vis:
            return vis[full], vis[full]
        for i in range(1, full):
            if i not in vis:
                continue
            for j in range(1, full):
                if j in vis and (i | j) == full:
                    return vis[i], vis[j]
        return -1, -1

    l = 0
    r = int(1e9)
    while l <= r:
        mid = (l + r) >> 1
        if check(mid) != (-1, -1):
            l = mid + 1
        else:
            r = mid - 1
    ans = check(r)
    print("%d %d" % (ans[0] + 1, ans[1] + 1))


if __name__ == "__main__":
    main(50)