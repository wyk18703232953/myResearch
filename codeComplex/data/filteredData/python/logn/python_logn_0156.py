def reach_max(n, k):
    return n * k + 1 - n * (n + 1) // 2


def main(n):
    # 根据规模 n 生成测试数据：构造一个 k，使得答案大致存在
    # 简单策略：令 k = 2 * n，保证 k 较大，一般可以覆盖 reach_max 的需求
    k = 2 * n

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
    # 示例：调用 main，规模 n 可在此修改
    main(10)