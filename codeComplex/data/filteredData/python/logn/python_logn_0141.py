def reach_max(n, k):
    return n * k + 1 - n * (n + 1) // 2


def main(n):
    """
    n: 问题规模，同时作为原程序中的 n。
    这里根据 n 构造测试数据 k，并复现原逻辑。
    可根据需要修改 k 的生成规则。
    """
    # 根据 n 生成测试数据，这里示例设定 k = max(2, n)
    k = max(2, n)

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


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的值
    main(10)