def main(n):
    """
    n 作为规模参数，用于生成测试数据 (x, k)。
    这里示例使用：
    - x = n
    - k = n 的平方
    可按需要修改生成策略。
    """
    mod = 10 ** 9 + 7

    # 根据 n 生成测试数据
    x = n
    k = n * n

    # 原逻辑
    if x == 0:
        ans = 0

    else:
        ans = (x * pow(2, k + 1, mod) - pow(2, k, mod) + 1 + mod) % mod

    # print(ans)
    pass
if __name__ == "__main__":
    # 默认用一个示例规模调用
    main(10)