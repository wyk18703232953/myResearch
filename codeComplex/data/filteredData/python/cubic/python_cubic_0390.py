from math import factorial

def main(n):
    mod = 10**9 + 7

    def binom(nn, m):
        return factorial(nn) // factorial(m) // factorial(nn - m)

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
    return ans


if __name__ == "__main__":
    # example deterministic call
    # print(main(10))
    pass