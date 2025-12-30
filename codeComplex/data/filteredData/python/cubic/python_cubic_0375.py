from math import factorial
import random

def binom(n, m):
    return factorial(n) // factorial(m) // factorial(n - m)

def build_mod(n):
    # 根据规模生成一个足够大的模数，这里取一个固定的大质数
    # 也可以改为与 n 有关，例如：10**9 + 7
    return 10**9 + 7

def foo(x, k, mod):
    ans = 0
    for i in range(k, 0, -1):
        sign = 1 if (i - k) % 2 == 0 else -1
        ans += sign * binom(k, i) * (i ** x)
        ans %= mod
    return ans

def f(x, k, mod):
    return (foo(x, k, mod) * pow(2, x - k, mod)) % mod

def main(n: int):
    # 根据 n 生成测试数据：这里 n 是原程序中的 n，模数自动生成
    mod = build_mod(n)

    ans = 0
    for i in range((n + 1) // 2):
        ans = (ans + f(n - i, i + 1, mod)) % mod

    print(ans)

if __name__ == "__main__":
    # 示例：运行规模为 10
    main(10)