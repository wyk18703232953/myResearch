def mypw2(deg: int) -> int:
    if deg >= 1500:
        return 2 ** 150
    return 2 ** deg


def sol(n: int, k: int):
    if k == 0:
        print("YES", n)
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
            print("YES", n - side)
            return
    print("NO")


def main(n: int):
    # 根据 n 生成测试数据：
    # 这里生成 t = n 组测试，每组 (n, k)：
    # k 从 0 到 n-1，简单线性递增，作为示例测试数据。
    t = n
    for i in range(t):
        k = i  # 可按需要调整测试数据生成方式
        sol(n, k)


if __name__ == "__main__":
    # 示例运行：可修改这里的 n 用于不同规模测试
    main(5)