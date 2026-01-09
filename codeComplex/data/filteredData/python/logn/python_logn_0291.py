mod = 1000000000 + 7

def qpow(base, exp, mod):
    """快速幂 base^exp % mod"""
    t = 1
    x = base % mod
    while exp > 0:
        if exp & 1:
            t = t * x % mod
        x = x * x % mod
        exp >>= 1
    return t

def main(n):
    # 根据 n 生成测试数据：
    # 原程序输入为 (n, m)，这里设 m = n 作为示例测试规模
    m = n

    if n == 0:
        # print(0)
        pass
        return

    ans = n * 2
    ans %= mod

    if m:
        t = qpow(2, m, mod)
        ans -= 1
        ans = (t * ans + 1) % mod

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)