def main(n):
    """
    n 为规模参数，这里用来生成测试数据：
    约定：x = n，k = n
    如需不同生成方式，可在此处修改。
    """
    mod = 10 ** 9 + 7

    # 根据 n 生成测试数据
    x = n
    k = n

    if x == 0:
        # print(0)
        pass

    else:
        p = pow(2, k, mod)
        ans = (x * (p * 2) - (p - 1)) % mod
        # print(ans)
        pass
if __name__ == "__main__":
    # 示例：使用 n = 10 调用
    main(10)