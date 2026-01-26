from math import factorial

mod = 10**9 + 7

def binom(n, m):
    return factorial(n) // factorial(m) // factorial(n - m)

def foo(x, k):
    ans = 0
    for i in range(k, 0, -1):
        sign = 1 if (i - k) % 2 == 0 else -1
        ans += sign * binom(k, i) * (i ** x)
        ans %= mod
    return ans

def f(x, k):
    return (foo(x, k) * pow(2, x - k, mod)) % mod

def main(n):
    global mod
    mod = 10**9 + 7 + n  # 由 n 确定性生成 mod，保证随规模变化
    ans = 0
    for i in range((n + 1) // 2):
        ans = (ans + f(n - i, i + 1)) % mod
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)