MOD = 1000000007

def main(n):
    """
    n 作为规模参数，用于生成测试数据。
    此处约定：
    x = n
    k = n
    如需不同的数据生成方式，可根据需要修改。
    """
    x = n
    k = n

    if x <= 0:
        return 0

    ans = (pow(2, k + 1, MOD) * x - pow(2, k, MOD) + 1) % MOD
    return ans

if __name__ == "__main__":
    # 示例：以 n = 10 运行
    n = 10
    # print(main(n))
    pass