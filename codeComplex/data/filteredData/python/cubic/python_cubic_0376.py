from math import factorial
import random

def binom(n, m):
    return factorial(n) // factorial(m) // factorial(n - m)

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
    # 根据 n 生成测试数据：这里随机生成 mod，保证 > 1
    random.seed(0)
    mod = random.randint(10**9 + 7, 10**9 + 7 + n + 1000)

    ans = 0
    for i in range((n + 1) // 2):
        ans = (ans + f(n - i, i + 1, mod)) % mod
    print(ans)

if __name__ == "__main__":
    # 示例：调用 main，规模 n 可按需修改
    main(10)