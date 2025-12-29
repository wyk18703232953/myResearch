def getsum(n: int) -> int:
    return ((1 << (2 * n)) - 1) // 3


def b(n: int, k: int):
    l = n - 1
    r = max(0, l - 41)
    while True:
        mid = (l + r) // 2
        count = getsum(n - mid)
        if count <= k:
            l = mid
        else:
            r = mid
        if l - r <= 1:
            break
        del count
    g = getsum(n - r)
    if g < k:
        del g
        return None
    elif g == k:
        del g
        return r
    return l


def main(n: int):
    """
    n 作为规模参数。
    这里根据 n 生成测试数据：
      - t = n
      - 对于第 i 组，设 N_i = i + 2（保证 N_i >= 2）
        K_i = getsum(N_i) // 2 作为一个中等规模的 k
    然后对每组 (N_i, K_i) 运行原来的逻辑并输出结果。
    """
    t = n
    for i in range(t):
        N = i + 2
        K = getsum(N) // 2  # 测试数据生成策略，可依据需要调整

        min_side = b(N, K)
        if min_side is None:
            print('NO')
            continue
        K -= getsum(N - min_side)
        if N == 2 and min_side == 1 and K == 2:
            print('NO')
            continue
        num_squares = (1 << (N - min_side)) * 2 - 1
        if K >= num_squares:
            print('YES ' + str(min_side - 1))
        else:
            print('YES ' + str(min_side))


if __name__ == "__main__":
    # 示例：调用 main(5) 进行测试
    main(5)