MOD = 1000000007

def mul(a, b, md):
    if b == 1:
        return a % md
    if b % 2 == 0:
        t = mul(a, b // 2, md)
        return (2 * t) % md
    return (mul(a, b - 1, md) + a) % md

def pows(a, b, md):
    if b == 0:
        return 1
    if b % 2 == 0:
        t = pows(a, b // 2, md)
        return mul(t, t, md) % md
    return mul(pows(a, b - 1, md), a, md) % md

def main(n):
    # 根据规模 n 生成测试数据：x 和 k
    # 这里示例生成方式为：
    # x = n，k = n 的平方再取模，保证非负且不过大
    x = n
    k = (n * n) % MOD

    ch = pows(2, k, MOD)
    ans = pows(2, k + 1, MOD) * x - ch + 1
    ans %= MOD
    if x == 0:
        ans = 0
    print(ans)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)