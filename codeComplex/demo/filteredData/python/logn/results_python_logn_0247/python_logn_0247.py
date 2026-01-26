MOD = 10**9 + 7

def main(n: int):
    """
    n 用来生成测试数据：
    - 当 n 为偶数时：x = n, k = n // 2
    - 当 n 为奇数时：x = n // 2, k = n
    返回计算结果。
    """
    # 根据 n 生成测试数据
    if n % 2 == 0:
        x = n
        k = n // 2

    else:
        x = n // 2
        k = n

    if x == 0:
        return 0
    return (x * pow(2, k + 1, MOD) - pow(2, k, MOD) + 1) % MOD


if __name__ == "__main__":
    # 示例：使用 n = 10 运行
    result = main(10)
    # print(result)
    pass