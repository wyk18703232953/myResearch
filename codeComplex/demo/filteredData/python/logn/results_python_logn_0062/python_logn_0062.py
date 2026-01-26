def main(n: int):
    # 根据规模 n 生成测试数据：
    # 这里生成一对 (l, r)，满足 0 <= l <= r < 2^n
    # 具体策略：取一个中间值 mid，构造 l, r
    if n <= 0:
        l, r = 0, 0

    else:
        # 限制 n 最大不超过 62（与原代码位宽一致）
        n_eff = min(n, 62)
        mid = (1 << (n_eff - 1))  # 2^(n_eff-1)
        l = mid
        r = (1 << n_eff) - 1      # 2^n_eff - 1

    # 下方为原逻辑的无 input 封装
    a = "{0:062b}".format(l)
    b = "{0:062b}".format(r)

    length = len(a)
    i = 0

    if l == r:
        # print(0)
        pass

    else:
        while i < length and a[i] == b[i]:
            i += 1
        # print(2 ** (62 - i) - 1)
        pass
if __name__ == "__main__":
    # 示例调用：可修改 n 测试不同规模
    main(10)