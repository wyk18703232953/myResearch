from math import factorial
from random import randint

def binom(n, m):
    return factorial(n) // factorial(m) // factorial(n - m)

def build_mod(n):
    # 生成一个与原逻辑兼容的模数（>1），这里简单取一个较大的质数
    # 也可以自行根据 n 设计其他规则
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

def main(n):
    # 根据 n 生成测试数据：此处只需要生成 mod
    mod = build_mod(n)

    ans = 0
    for i in range((n + 1) // 2):
        ans = (ans + f(n - i, i + 1, mod)) % mod
    print(ans)

if __name__ == "__main__":
    # 示例：调用 main，n 可按需修改或由外部测试框架调用
    main(10)