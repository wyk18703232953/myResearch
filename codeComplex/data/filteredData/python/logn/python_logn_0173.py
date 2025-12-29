def is_good(x, n, k):
    y = k - x + 1
    return (y + k * (k - 1) // 2 - y * (y - 1) // 2) >= n


def solve(n, k):
    if n == 1:
        return 0
    if (k + (k - 2) * (k - 1) // 2) < n:
        return -1
    if k >= n:
        return 1

    l = 0
    r = k
    while r > l + 1:
        m = (l + r) // 2
        if is_good(m, n, k):
            r = m
        else:
            l = m
    return r


def main(n):
    """
    n: 规模参数，用于生成测试数据。
    这里根据 n 构造一组 (n, k) 测试数据：
    - 保证 k >= 2，k 不小于 n/2，避免过多 -1 情况。
    """
    if n < 2:
        n_val = 1
        k_val = 1
    else:
        n_val = n
        k_val = max(2, n // 2)

    ans = solve(n_val, k_val)
    print(ans)


if __name__ == "__main__":
    # 示例调用：可按需修改 n 的值进行测试
    main(10)