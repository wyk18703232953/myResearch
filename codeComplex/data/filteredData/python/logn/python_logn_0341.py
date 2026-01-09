MOD = 1000000007

def main(n: int):
    # 根据 n 生成测试数据：
    # 这里示例：令 x = n，k = n 的平方
    x = n
    k = n * n

    if x != 0:
        ans = (pow(2, k, MOD) * (2 * x - 1) + 1) % MOD

    else:
        ans = 0

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)