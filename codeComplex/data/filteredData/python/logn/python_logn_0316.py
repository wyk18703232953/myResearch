def power(x, y, mod=1000000007):
    res = 1
    while y > 0:
        if y & 1:
            res = (res * x) % mod
        y >>= 1
        x = (x * x) % mod
    return res


def main(n):
    """
    按规模 n 生成测试数据并计算结果。
    这里示例性地用 n 来生成 x, k：
      x = n
      k = n
    如需其他生成策略，可在此处修改。
    """
    mod = 1000000007

    # 根据 n 生成测试数据（示例）
    x = n
    k = n

    factor = power(2, k, mod)
    ans = ((2 * factor * x) % mod - factor % mod + 1 + mod) % mod

    if x == 0:
        print("0")
    else:
        print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)