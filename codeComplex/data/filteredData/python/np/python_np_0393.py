from collections import Counter
import random

def check(a, mid, n, m, z):
    b = Counter()
    for i in range(n):
        c = ["0"] * m
        for j in range(m):
            if a[i][j] >= mid:
                c[j] = "1"
        zz = int("".join(c), 2)
        b[zz] = i
    c = list(b.keys())
    lc = len(c)
    for i in range(lc):
        for j in range(i, lc):
            if c[i] | c[j] == z:
                mi, x, y = 10**10, b[c[i]], b[c[j]]
                for k in range(m):
                    mi = min(mi, max(a[x][k], a[y][k]))
                if mi >= mid:
                    return (x, y)

def main(n):
    # 生成测试数据：
    # n：行数（给定）
    # m：列数，这里设为 min(n, 10) 以保证复杂度适中
    m = max(1, min(n, 10))
    # 元素值范围 [0, 10^9]
    a = [[random.randint(0, 10**9) for _ in range(m)] for _ in range(n)]

    lo, hi = 0, 10**9
    ans = [1, 1]
    y = (1 << m) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        z = check(a, mid, n, m, y)
        if z:
            lo = mid + 1
            ans = [z[0] + 1, z[1] + 1]
        else:
            hi = mid - 1

    print(*ans)

if __name__ == "__main__":
    # 示例：调用 main(5) 生成规模为 5 的随机测试数据并运行逻辑
    main(5)