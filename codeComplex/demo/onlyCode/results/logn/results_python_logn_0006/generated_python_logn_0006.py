def main(n: int):
    # 根据规模 n 生成测试数据，这里构造一对 l, r
    # 让它们在二进制上有 n 位不同，例如：
    # l = 0, r = (1 << n) - 1  => l ^ r 的低 n 位全为 1
    l = 0
    r = (1 << n) - 1

    # 原逻辑开始
    target, final = l ^ r, 1
    while target:
        target >>= 1
        final <<= 1
    print(final - 1)


if __name__ == "__main__":
    # 示例：n = 3 时，对应 l=0, r=7，输出应为 7
    main(3)