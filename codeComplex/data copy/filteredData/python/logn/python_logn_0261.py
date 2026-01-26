def main(n: int):
    """
    将原程序改为无 input() 的形式。
    这里根据规模 n 生成测试数据：
    - x = n
    - k = n^2
    """
    x = n
    k = n * n

    if x == 0:
        # print(0)
        pass
        return

    x = 2 * x - 1
    mod = 10**9 + 7

    def pot(r, k):
        if k == 0:
            return 1
        if k % 2 == 1:
            return r * pot(r, k - 1) % mod
        y = pot(r, k // 2)
        return y * y % mod

    # print((pot(2, k) * x + 1) % mod)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)