MOD = 1000000007

def main(n):
    """
    n 为规模参数，用来生成测试数据 (x, k)。
    这里示例使用：
        x = n
        k = n
    如需其他策略，可自行修改。
    """
    x = n
    k = n

    pw = pow(2, k + 1, MOD)
    t = pow(2, k, MOD)
    a = (pw * x) - t
    a = (a + 1) % MOD
    if x == 0:
        a = 0
    # print(int(a))
    pass
if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)