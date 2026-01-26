MOD = 1000000007

def main(n):
    """
    按规模 n 生成测试数据 (x, k)，并计算原逻辑的结果。
    这里示例生成方式为：
        x = n
        k = n
    可根据需要修改生成规则。
    """
    # 生成测试数据
    x = n
    k = n

    if x > 0:
        ans = (pow(2, k + 1, MOD) * x) % MOD
        ans = (ans - pow(2, k, MOD)) % MOD
        ans = (ans + 1) % MOD

    else:
        ans = 0

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)