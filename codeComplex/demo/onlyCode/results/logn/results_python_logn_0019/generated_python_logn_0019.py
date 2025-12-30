def main(n: int):
    """
    规模 n 用来生成一组 (l, r) 测试数据：
    - 保证 0 <= l < r
    - l, r 的大小大约在 [0, 2^n) 内
    你可根据需要自行调整生成方式。
    这里采用简单可预测的生成方案：
        l = 2^(n-1) - 1   (当 n>0 时)
        r = 2^n - 1
    当 n <= 1 时，特殊处理以保证 l < r。
    """

    if n <= 1:
        l, r = 0, 1
    else:
        l = (1 << (n - 1)) - 1
        r = (1 << n) - 1

    # 原始逻辑开始
    if l == r:
        print(0)
        return

    binr, binl = list(bin(r)[2:]), list(bin(l)[2:])
    binl = ['0'] * (len(binr) - len(binl)) + binl

    for i in range(len(binl)):
        if binl[i] != binr[i]:
            binl = '1' * (len(binl[i:]))
            break

    print(int(binl, 2))


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)