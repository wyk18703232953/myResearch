def main(n):
    # 输入结构：
    # 行1: n, k
    # 行2: n 个整数
    #
    # 将参数 n 直接作为数组长度；
    # k 选择一个随 n 增长、但不小于 1 的确定性值。
    if n <= 0:
        print(0)
        return

    k = max(1, n.bit_length())  # 与 n 相关的确定性 k 值

    # 构造长度为 n 的确定性整数序列
    arr = [(i * 17 + 23) ^ (i // 2) for i in range(n)]

    d = dict()
    d[0] = 1
    x = 0
    for val in arr:
        x ^= val
        v = min(x, (1 << k) - x - 1)
        if v not in d:
            d[v] = 0
        d[v] += 1

    ans = 0
    for _, v in d.items():
        c1 = v // 2
        c2 = v - c1
        ans += c1 * (c1 - 1) // 2 + c2 * (c2 - 1) // 2

    print(n * (n - 1) // 2 + n - ans)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(10)