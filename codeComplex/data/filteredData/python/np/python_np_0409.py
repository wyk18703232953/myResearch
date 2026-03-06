def bs(a, mid, ans, n, m):
    can = [0 for _ in range(1 << m)]
    for i in range(n):
        t = 0
        for j in range(m):
            t = (t << 1) | (a[i][j] >= mid)
        can[t] = i + 1
    for i in range(1 << m):
        if not can[i]:
            continue
        for j in range(1 << m):
            if not can[j]:
                continue
            if i | j == (1 << m) - 1:
                ans[0] = can[i]
                ans[1] = can[j]
                return 1
    return 0


def main(n):
    # 映射：n -> 行数，列数 m 取一个固定小值以控制 2^m 规模
    # 保持可规模化：时间复杂度主要随 n 线性、随 2^m 二次
    m = 5
    # 构造确定性矩阵 a，值范围控制在 0..100
    # 使用简单算术生成：a[i][j] = (i * (j + 3) + j * j) % 101
    a = [[(i * (j + 3) + j * j) % 101 for j in range(m)] for i in range(n)]

    l = 0
    r = 100000000000
    ans = [1, 1]
    while l <= r:
        mid = (l + r) // 2
        if bs(a, mid, ans, n, m):
            l = mid + 1
        else:
            r = mid - 1
    print(*ans)


if __name__ == "__main__":
    main(1000)