def reach_max(n, k):
    return n * k + 1 - n * (n + 1) // 2


def main(n):
    """
    n: 规模参数，用来生成测试数据。
    我们令 k = 2 * n（可根据需要修改生成规则）。
    原本程序期望输入为: n k
    这里将“问题中的 n”记为 target，k 按规则生成。
    """
    target = n
    k = 2 * n  # 测试数据生成规则，可调整

    if target == 1:
        print(0)
        return

    lo, hi = 1, k - 1

    if target > reach_max(hi, k):
        print(-1)
        return

    while lo < hi:
        mid = (lo + hi) // 2
        if reach_max(mid, k) < target:
            lo = mid + 1
        else:
            hi = mid

    print(lo)


if __name__ == "__main__":
    # 示例：以 n=10 作为规模参数运行
    main(10)