def mypw2(deg: int) -> int:
    if deg >= 1500:
        return 2 ** 150
    return 2 ** deg


def sol(n: int, k: int):
    if k == 0:
        # print("YES", n)
        pass
        return
    for side in range(1, n + 1):
        MIN = mypw2(side + 1) - side - 2
        MAX = (
            mypw2(2 * n)
            - mypw2(2 * n - side + 1)
            + mypw2(side + 1)
            + mypw2(2 * n - 2 * side)
            - 2
        )
        MAX //= 3
        if MIN <= k <= MAX:
            # print("YES", n - side)
            pass
            return
    # print("NO")
    pass


def main(n: int):
    """
    n: 问题规模。这里用 n 同时作为原题中的 n，
       并生成若干组 (n, k) 的测试数据。
    可以根据需要修改测试数据生成策略。
    """
    # 示例：生成一组或多组测试数据，这里简单给出几种典型 k
    test_ks = [
        0,                  # 边界情况
        max(0, n // 2),     # 中等范围
        max(0, n * n // 3)  # 稍大一些的 k
    ]

    for k in test_ks:
        sol(n, k)


if __name__ == "__main__":
    # 调用 main，给一个默认的规模 n，可按需修改
    main(10)