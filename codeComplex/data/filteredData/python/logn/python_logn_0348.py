MOD = 1000000007

def solve(x, k):
    if x == 0:
        return 0
    return (pow(2, k, MOD) * ((2 * x - 1) % MOD) + 1) % MOD

def main(n):
    """
    n 为规模参数，用于生成测试数据。
    这里简单生成一组 (x, k) 测试数据：
    x = n
    k = n
    根据需要可修改为更复杂的生成方式。
    """
    x = n
    k = n
    ans = solve(x, k)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)