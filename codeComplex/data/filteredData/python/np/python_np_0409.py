import random

def bs(a, mid, ans, n, m):
    can = [0] * (1 << m)
    for i in range(n):
        t = 0
        for j in range(m):
            t = (t << 1) | (a[i][j] >= mid)
        can[t] = i + 1

    full_mask = (1 << m) - 1
    for i in range(1 << m):
        if not can[i]:
            continue
        for j in range(1 << m):
            if not can[j]:
                continue
            if (i | j) == full_mask:
                ans[0] = can[i]
                ans[1] = can[j]
                return 1
    return 0


def main(n):
    # 规模 n 作为行数；列数 m 可根据需要设置，这里设为 5
    m = 5

    # 生成测试数据：n 行 m 列的随机整数（0 ~ 1e9）
    a = [[random.randint(0, 10**9) for _ in range(m)] for _ in range(n)]

    l = 0
    r = 10**11
    ans = [1, 1]
    while l <= r:
        mid = (l + r) // 2
        if bs(a, mid, ans, n, m):
            l = mid + 1
        else:
            r = mid - 1

    print(ans[0], ans[1])


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)