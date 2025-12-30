def main(n: int):
    mod = 10 ** 9 + 7
    # 根据规模 n 生成测试数据，这里简单生成：
    # x = n, k = n
    x = n
    k = n

    if x == 0:
        print(0)
        return
    if k == 0:
        print(2 * x % mod)
        return

    ans = pow(2, k + 1, mod)
    ans *= x
    ans %= mod
    ans -= pow(2, k, mod)
    ans += 1
    ans %= mod
    ans += mod
    ans %= mod

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)