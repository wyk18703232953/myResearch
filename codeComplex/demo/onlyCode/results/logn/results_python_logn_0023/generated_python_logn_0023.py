def main(n: int):
    # 根据规模 n 生成测试数据：构造区间 [l, r]
    # 这里简单设为 l = 0, r = (1 << n) - 1（即 n 位全 1），也可按需修改
    l = 0
    r = (1 << n) - 1

    for i in range(61)[::-1]:
        if (l >> i) & 1 != (r >> i) & 1:
            print((1 << (i + 1)) - 1)
            return
    print(0)


if __name__ == "__main__":
    # 示例：调用 main(5) 表示使用 n=5 规模的测试数据
    main(5)