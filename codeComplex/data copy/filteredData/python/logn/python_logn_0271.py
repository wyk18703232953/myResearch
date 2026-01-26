MOD = 10**9 + 7

def main(n: int):
    # 根据规模 n 生成测试数据
    # 这里示例：令 x = n, k = n 的平方
    x = n
    k = n * n

    if x == 0:
        result = 0

    else:
        result = ((2 * x - 1) * pow(2, k, MOD) + 1) % MOD

    # print(result)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)