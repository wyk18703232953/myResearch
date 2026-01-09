from math import factorial

def binom(n, m):
    return factorial(n) // factorial(m) // factorial(n - m)

def main(n):
    # 生成测试用模数，这里固定为较大的质数，避免除零等问题
    mod = 10**9 + 7

    def foo(x, k):
        ans = 0
        for i in range(k, 0, -1):
            sign = 1 if (i - k) % 2 == 0 else -1
            ans += sign * binom(k, i) * (i ** x)
            ans %= mod
        return ans

    def f(x, k):
        return (foo(x, k) * pow(2, x - k, mod)) % mod

    ans = 0
    for i in range((n + 1) // 2):
        ans = (ans + f(n - i, i + 1)) % mod

    # print(ans)
    pass
    return ans

if __name__ == "__main__":
    # 示例：自动生成规模为 10 的测试数据
    main(10)