MOD = 1000000007

def main(n: int) -> int:
    """
    根据规模 n 生成测试数据 x, k，并计算原程序中的结果。
    测试数据方案：
      x = n
      k = n
    返回计算结果 ans（与原程序逻辑一致）。
    """
    x = n
    k = n

    mul = pow(2, k + 1, MOD)
    y = (x % MOD * mul) % MOD
    ans = y
    if x != 0:
        ans = (ans % MOD - (pow(2, k, MOD) - 1) % MOD) % MOD

    return ans


if __name__ == "__main__":
    # 示例：手动指定规模 n 进行测试
    n = 10
    result = main(n)
    print(result)