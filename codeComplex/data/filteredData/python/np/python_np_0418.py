import random

def check(x: int, a, n, m) -> (int, int):
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


def main(n: int):
    # 规模 n 表示行数，列数 m 可从 n 派生或固定，这里设为 min(8, n)
    m = min(8, max(1, n))  # 保证 1 <= m <= 8

    # 生成测试数据 a：n 行 m 列的随机整数
    # 为了保持二分查找区间的合理性，值域设为 [0, 1e9]
    a = [[random.randint(0, 10**9) for _ in range(m)] for _ in range(n)]

    l = 0
    r = 10**9
    while l <= r:
        mid = (l + r) >> 1
        if check(mid, a, n, m) != (-1, -1):
            l = mid + 1
        else:
            r = mid - 1
    ans = check(r, a, n, m)
    # 若不存在可行解，ans 为 (-1, -1)，保持原始代码 +1 行为
    print("%d %d" % (ans[0] + 1, ans[1] + 1))


if __name__ == '__main__':
    # 示例：调用 main，n 可以根据需要修改
    main(5)