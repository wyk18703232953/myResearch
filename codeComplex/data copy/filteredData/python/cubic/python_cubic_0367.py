from math import factorial

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
    mod = 10**9 + 7
    ans = 0
    for i in range((n + 1) // 2):
        ans = (ans + f(n - i, i + 1, mod)) % mod
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)