def main(n: int):
    """
    使用规模 n 生成测试数据 (l, r)，并执行原逻辑：
    - 生成 1 <= l <= r <= 2^n - 1
    - 输出结果
    """
    if n <= 1:
        # 对于 n<=1，没有有效的 1 <= l <= r <= 2^n - 1 且 l<r 的整数对
        # 按原逻辑输出 0（等价于 l==r 的情况）
        print(0)
        return

    # 生成测试数据：
    # 选择最大范围内的两个值，保证 l < r
    # 这里简单设定：l = 2^(n-1), r = 2^n - 1
    l = 1 << (n - 1)
    r = (1 << n) - 1

    if l == r:
        print(0)
        return

    binr, binl = list(bin(r)[2:]), list(bin(l)[2:])
    binl = ['0'] * (len(binr) - len(binl)) + binl

    for i in range(len(binl)):
        if binl[i] != binr[i]:
            del binl[0:i]
            del binr[0:i]
            break

    x = '1' * len(binl)
    l = int(x, 2)
    print(l)


if __name__ == "__main__":
    # 示例：调用 main(5)，可自行修改 n 测试
    main(5)