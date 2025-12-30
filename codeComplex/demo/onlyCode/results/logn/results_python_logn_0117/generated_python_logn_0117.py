def main(n):
    """
    n: 控制测试数据规模，这里用来生成一个 (L, R) 区间：
       L 在 [0, 2^k) 内，R 在 [L, 2^k) 内，其中 k = max(1, n.bit_length())。
    返回：原 solve() 的输出结果。
    """
    # 根据 n 生成测试数据 (L, R)
    if n <= 1:
        L, R = 0, 1
    else:
        k = max(1, n.bit_length())
        # 让 L 接近 n，R 为同数量级的上界
        L = max(0, n - (1 << (k - 1)))
        R = (1 << k) - 1
        if L == R:
            L = max(0, L - 1)

    L, R = int(L), int(R)

    if L == R:
        return 0
    l = len(bin(L)[2:])
    r = len(bin(R)[2:])
    while l == r:
        L -= 2 ** (r - 1)
        R -= 2 ** (r - 1)
        l = len(bin(L)[2:])
        r = len(bin(R)[2:])
    return 2 ** r - 1


if __name__ == "__main__":
    # 示例：可在此处修改 n 以运行测试
    print(main(10))