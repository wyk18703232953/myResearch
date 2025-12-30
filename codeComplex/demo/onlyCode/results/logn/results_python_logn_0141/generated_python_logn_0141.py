def reach_max(n, k):
    return n * k + 1 - n * (n + 1) // 2


def main(n):
    """
    n 为规模参数，用来生成测试数据。
    这里构造一个与规模 n 相关的 k，使得 1 <= n <= reach_max(k-1, k) 大致有意义。
    简单选择 k = max(2, n // 2 + 1) 作为测试。
    """
    if n <= 0:
        # 原逻辑中 n 需要是正整数，这里直接返回不做处理
        return

    # 生成测试数据：选择一个依赖于规模 n 的 k
    k = max(2, n // 2 + 1)

    # 以下是原逻辑，只是用上面生成的 n, k 替代 input()
    if n == 1:
        print(0)
        return

    lo, hi = 1, k - 1

    if n > reach_max(hi, k):
        print(-1)
        return

    while lo < hi:
        mid = (lo + hi) // 2
        if reach_max(mid, k) < n:
            lo = mid + 1
        else:
            hi = mid

    print(lo)


# 示例调用
if __name__ == "__main__":
    # 可以在此修改 n 以进行不同规模的测试
    main(10)