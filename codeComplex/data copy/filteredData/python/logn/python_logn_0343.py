MOD = 10 ** 9 + 7

def main(n: int):
    # 生成测试数据：
    # n 控制 x 的大小量级，k 用 n 的一部分控制
    # 确保 x >= 0, k >= 0
    x = n
    k = n // 2

    if x == 0:
        result = 0

    else:
        result = ((2 * x - 1) * pow(2, k, MOD) + 1) % MOD

    # print(result)
    pass
if __name__ == "__main__":
    # 示例：可以在此处指定 n 进行测试
    main(10)