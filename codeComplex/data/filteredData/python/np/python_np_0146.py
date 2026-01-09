def main(n: int):
    # 生成规模为 n 的测试数据，这里将 m 取为 0..(2^n - 1) 里的一个值
    # 为了有一定变化，选 m = (2^n - 1) // 3
    if n <= 0:
        return
    max_m = (1 << n) - 1
    m = max_m // 3

    a = [0 for _ in range(n)]
    l, r = 0, n - 1
    m -= 1

    for i in range(1, n + 1):
        cur = 2 ** (n - i - 1)
        if m >= cur:
            m -= cur
            a[r] = i
            r -= 1

        else:
            a[l] = i
            l += 1

    # print(*a)
    pass
if __name__ == "__main__":
    # 示例运行，可修改 n 测试不同规模
    main(5)