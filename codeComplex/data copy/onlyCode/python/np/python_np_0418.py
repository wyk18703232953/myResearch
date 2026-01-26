def check(x: int) -> (int, int):
    vis = {}
    for i, array in enumerate(a):
        t = 0
        for j, val in enumerate(array):
            if val >= x:
                t |= 1 << j
        vis[t] = i
    if (1 << m) - 1 in vis:
        return vis[(1 << m) - 1], vis[(1 << m) - 1]
    for i in range(1, (1 << m) - 1):
        for j in range(1, (1 << m) - 1):
            if i in vis and j in vis and i | j == (1 << m) - 1:
                return vis[i], vis[j]
    return -1, -1


if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    l = 0
    r = int(1e9)
    while l <= r:
        mid = l + r >> 1
        if check(mid) != (-1, -1):
            l = mid + 1
        else:
            r = mid - 1
    ans = check(r)
    print("%d %d" % (ans[0] + 1, ans[1] + 1))
