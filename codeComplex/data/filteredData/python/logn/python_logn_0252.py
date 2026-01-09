def main(n):
    """
    n: 规模参数，用来生成测试数据
    测试数据生成方式：x = n, k = n
    如需其他生成规则，可自行修改。
    """
    x = n
    k = n
    m = 10**9 + 7

    if x > 0:
        ans = (x * pow(2, k + 1, m) - pow(2, k, m) + 1) % m

    else:
        ans = 0

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)