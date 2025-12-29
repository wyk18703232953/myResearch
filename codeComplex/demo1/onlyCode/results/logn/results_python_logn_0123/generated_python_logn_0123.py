def solve_one(n, k):
    s = k * (k + 1) // 2
    if s < n:
        return -1

    l = 1
    r = k
    while l <= r:
        mid = (l + r) // 2
        curr = s - (mid * (mid - 1)) // 2

        if curr == n:
            return k - mid + 1
        elif curr < n:
            r = mid - 1
        else:
            l = mid + 1

    return k - l + 2


def main(n):
    """
    规模参数 n：用于生成一组测试数据 (N, K)，并返回原程序的输出结果。
    这里简单设定：
        N = n + 1
        K = n + 1
    使得 n' = N - 1 = n, k' = K - 1 = n，与原逻辑保持一致。
    """
    N = n + 1
    K = n + 1

    n_adj = N - 1
    k_adj = K - 1

    if n_adj == 0:
        return 0
    else:
        return solve_one(n_adj, k_adj)


if __name__ == "__main__":
    # 示例：调用 main(10)，可根据需要修改或在外部调用 main(n)
    print(main(10))