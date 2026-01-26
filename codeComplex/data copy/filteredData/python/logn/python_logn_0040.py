def main(n: int):
    # 根据规模 n 生成测试数据：构造一个区间 [l, r]
    # 示例策略：让 r = (1 << n) - 1，l = 0，这样可测试到最大二进制长度为 n 的情况
    if n <= 0:
        return

    l = 0
    r = (1 << n) - 1

    s = bin(l)[2:]
    t = bin(r)[2:]
    z = max(len(s), len(t))
    s = '0' * (z - len(s)) + s
    t = '0' * (z - len(t)) + t

    i = 0
    while i < z and s[i] == t[i]:
        i += 1

    result = pow(2, z - i) - 1
    # print(result)
    pass
if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)