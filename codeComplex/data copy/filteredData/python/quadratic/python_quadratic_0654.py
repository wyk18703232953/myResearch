from math import factorial

def binom(n, m):
    return factorial(n) // factorial(m) // factorial(n - m)

def main(n):
    # Deterministically derive n and mod from input scale n
    # Ensure positive n for meaningful behavior
    if n <= 0:
        n_local = 1

    else:
        n_local = n
    # Use a fixed prime-based modulus function of n for determinism
    mod = 10**9 + 7 + (n_local % 10)

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
    for i in range((n_local + 1) // 2):
        ans = (ans + f(n_local - i, i + 1)) % mod
    # print(ans)
    pass
    return ans

if __name__ == "__main__":
    # Example deterministic call; change n here for experiments
    main(10)