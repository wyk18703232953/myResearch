def power(x, y, p):
    res = 1
    x = x % p
    if x == 0:
        return 0
    while y > 0:
        if y & 1:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res


def main(n):
    """
    n: 规模参数，用来生成测试数据 (x, k)
    这里采用简单的生成策略：
      x = n
      k = n + 1
    可按需要自行修改生成逻辑。
    """
    p = 1000000007

    # 生成测试数据
    x = n
    k = n + 1

    if x == 0:
        # print("0")
        pass

    else:
        t = (((power(2, k, p)) * ((2 * x - 1) % p)) % p + 1) % p
        # print(t)
        pass
if __name__ == "__main__":
    # 示例：用 n = 10 运行
    main(10)