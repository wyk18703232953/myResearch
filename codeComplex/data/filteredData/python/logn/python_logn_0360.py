def main(n: int):
    """
    根据规模 n 生成测试数据并执行原逻辑。
    测试数据生成规则（可按需要修改）：
      x = n
      k = n 的二进制位数（至少为 1）
    """
    mod = 1000000007

    # 生成测试数据
    x = n
    k = max(1, n.bit_length())

    if x == 0:
        print(0)
        return

    a = pow(2, k, mod) % mod
    b = (2 * a) % mod
    ans = (((((x % mod) * (b % mod)) % mod) - (a % mod) + 1) + mod) % mod
    print(ans)


if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)