def pow_mod(x, pwr, mod):
    res = 1
    multiplier = x
    while pwr > 0:
        if pwr % 2 == 1:
            res = res * multiplier % mod
        multiplier = multiplier * multiplier % mod
        pwr //= 2
    return res


def main(n):
    # 根据 n 生成测试数据: 让 x = n, k = n^2 作为示例规模
    x = n
    k = n * n

    MOD = 1000000007

    if x == 0:
        res = 0
    else:
        res = pow_mod(2, k + 1, MOD) * x % MOD
        res = (res - pow_mod(2, k, MOD)) % MOD
        res = (res + 1) % MOD

    print(res)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)