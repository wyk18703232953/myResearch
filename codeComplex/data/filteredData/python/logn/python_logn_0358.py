def main(n: int):
    """
    n 作为规模参数，用来生成测试数据 (x, k)。
    这里示例性地根据 n 构造：
      x = n
      k = n // 2
    可根据需要自行修改生成规则。
    """
    mod = 10**9 + 7

    # 根据 n 生成测试数据
    x = n
    k = n // 2

    if x == 0:
        print(0)
        return
    if k == 0:
        print(x * 2 % mod)
        return

    ans = pow(2, k + 1, mod)
    ans *= x
    ans %= mod
    ans -= pow(2, k, mod) - 1
    ans %= mod
    ans += mod
    ans %= mod
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)