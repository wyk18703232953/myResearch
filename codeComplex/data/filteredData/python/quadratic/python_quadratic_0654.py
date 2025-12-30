from math import factorial
import random

def binom(n, m):
    return factorial(n) // factorial(m) // factorial(n - m)

def make_mod(n):
    # 简单生成一个与 n 相关、但固定范围内的模数
    # 这里使用一个大质数附近的值，避免过小导致大量取模为 0
    base_prime = 10**9 + 7
    return base_prime - (n % 1000)

def foo(x, k, mod):
    ans = 0
    for i in range(k, 0, -1):
        sign = 1 if (i - k) % 2 == 0 else -1
        ans += sign * binom(k, i) * (i ** x)
        ans %= mod
    return ans

def f(x, k, mod):
    return (foo(x, k, mod) * pow(2, x - k, mod)) % mod

def main(n):
    # 根据 n 生成测试数据：这里自动生成 mod
    # 也可以根据需要改成随机或其他规则生成
    mod = make_mod(n)

    ans = 0
    for i in range((n + 1) // 2):
        ans = (ans + f(n - i, i + 1, mod)) % mod
    print(ans)

if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可按需修改或由外部调用 main(n)
    main(10)