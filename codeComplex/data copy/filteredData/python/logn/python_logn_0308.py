MOD = 10**9 + 7

def main(n: int) -> int:
    """
    n: 规模参数，用于生成测试数据并计算结果。
    这里根据 n 生成 x，例如令 x = n。
    如需其他测试数据策略，可在此修改。
    """
    x = n  # 根据 n 生成测试数据，这里简单设为 x = n

    c = 4 * x
    if c == 0:
        ans = 0
    elif n == 0:
        ans = 2 * x

    else:
        ans = (((c - 2) * pow(2, n - 1, MOD) + 1) + MOD) % MOD

    return ans % MOD


# 示例：需要时可以调用 main(n)
# print(main(10))