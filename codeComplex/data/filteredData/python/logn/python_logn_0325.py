MOD = 1000000007

def main(n: int):
    # 根据规模 n 生成测试数据
    # 这里简单设定：x = n，k = n，用户可按需修改生成策略
    x = n
    k = n

    if x == 0:
        print(0)
    else:
        # pow(2, k, MOD) 为 2^k mod MOD
        result = (pow(2, k, MOD) * ((2 * x - 1) % MOD) + 1) % MOD
        print(result)


if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时按需修改 n
    main(10)