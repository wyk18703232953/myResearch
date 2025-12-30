def main(n):
    """
    n 为规模，用于生成测试数据 (x, k)。
    这里示例生成方式为：
      x = n
      k = n 的二进制长度
    实际可按需要替换生成逻辑。
    """
    mod = 1000000007

    # 示例测试数据生成逻辑
    x = n
    k = max(0, n.bit_length() - 1)  # 避免负数

    if x == 0:
        ans = 0
    else:
        ans = x * pow(2, k + 1, mod) - pow(2, k, mod) + 1
        ans %= mod

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)