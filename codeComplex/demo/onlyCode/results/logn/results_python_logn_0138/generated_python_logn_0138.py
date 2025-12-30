def solve(n, k):
    k -= 1
    lo, hi = 0, int(1e9)
    while lo < hi:
        m = (lo + hi + 1) // 2
        if 1 + k * (k + 1) // 2 - m * (m + 1) // 2 >= n:
            lo = m
        else:
            hi = m - 1
    if 1 + k * (k + 1) // 2 - lo * (lo + 1) // 2 >= n:
        lo = k - lo
    else:
        lo = -1
    return lo


def main(n):
    # 生成测试数据：n 为规模参数
    # 这里令 k 与 n 同阶，例如 k = n + 5，且保证 k >= 1
    k = max(1, n + 5)
    ans = solve(n, k)
    print(ans)


if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)