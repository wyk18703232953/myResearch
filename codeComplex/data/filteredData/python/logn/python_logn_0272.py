mod = 1000000007

def fastexp(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base % mod
    t = fastexp(base, exp // 2)
    if exp % 2 == 0:
        return (t % mod * t % mod) % mod
    else:
        return (t % mod * t % mod * base % mod) % mod

def main(n):
    # 根据规模 n 生成测试数据：
    # 这里简单设定：x = n, k = n（可按需要修改生成方式）
    x = n
    k = n

    if x == 0:
        print(0)
        return

    t = fastexp(2, k) % mod
    before = ((2 * t) % mod * x % mod) % mod - (t + mod - 1) % mod
    while before < 0:
        before += mod
    before = before % mod
    print(before)

if __name__ == "__main__":
    # 示例：使用 n = 10 运行
    main(10)