MOD = int(1e9 + 9)

def fast_power(x, y):
    res = 1
    while y > 0:
        if y % 2 == 1:
            res = res * x % MOD
        x = x * x % MOD
        y //= 2
    return res

def main(n):
    """
    参数 n 为规模，用于生成测试数据 (n, m, k)。
    可根据需要修改下面的生成规则。
    """
    # 简单示例数据生成规则：
    # n 为输入规模
    # m 在 [0, n] 内
    # k 在 [1, n] 内
    # 这里只是一个确定性的示例，可按需求替换为更复杂/随机的生成方式
    m = n // 2 if n > 0 else 0
    k = max(1, n // 3)  # 确保 k >= 1

    x = max(0, m - n // k * (k - 1) - n % k)
    z = (m - x * k) % MOD
    res = fast_power(2, x + 1)
    res = (res - 2) % MOD * k % MOD
    res = (res + z) % MOD
    print(res)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)