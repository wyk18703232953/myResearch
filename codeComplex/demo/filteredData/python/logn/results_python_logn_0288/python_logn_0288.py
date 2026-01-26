MOD = 1000000007

def bin_func(n: int) -> int:
    if n == 0:
        return 1

    else:
        if n % 2 == 1:
            return bin_func(n - 1) * 2

        else:
            b = bin_func(n // 2) % MOD
            return b * b

def main(n: int):
    """
    n 为规模参数，用于生成测试数据 (x, k)。

    这里示例生成方式为：
    x = n + 1
    k = n
    可根据需要修改生成规则。
    """
    x = n + 1
    k = n

    if x == 0:
        # print(0)
        pass

    else:
        z = bin_func(k + 1) % MOD
        z = z * (x - 1)
        z = z % MOD
        z += bin_func(k)
        z += 1
        while z < 0:
            z += MOD
        # print(z % MOD)
        pass
if __name__ == "__main__":
    # 示例：调用 main(10)，可根据需要修改 n
    main(10)