def main(n: int):
    # 根据规模 n 生成一组 (l, r) 测试数据
    # 这里设定：l = 2^n，r = 2^{n+1} - 1，保证 l < r 且差距较大
    if n <= 0:
        l, r = 0, 0

    else:
        l = 1 << n
        r = (1 << (n + 1)) - 1

    # 以下为原逻辑（去掉 input() 后的形式）
    if l == r:
        # print(0)
        pass
        return
    mx = str(bin(l ^ r))
    x = len(mx[2:])
    # print(2 ** x - 1)
    pass
if __name__ == "__main__":
    # 示例：以 n = 3 运行
    main(3)