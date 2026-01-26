mod = 1000000007
import math

def powm(a, n, m):
    if a == 1 or n == 0:
        return 1
    if n % 2 == 0:
        s = powm(a, n // 2, m)
        return s * s % m

    else:
        return a * powm(a, n - 1, m) % m

def modInverse(b, m):
    g = math.gcd(b, m)
    if g != 1:
        return -1

    else:
        return pow(b, m - 2, m)

def modDivide(a, b, m):
    a = a % m
    inv = modInverse(b, m)
    a = (a * inv) % m
    return a

def original_logic(n, k):
    ans = (powm(4, k, mod) * n) % mod
    r = powm(2, k, mod)
    r = (powm(r, 2, mod) - r) % mod
    w = modDivide(r, 2, mod)
    ans = (ans - w) % mod
    er = powm(2, k, mod)
    ans = modDivide(ans, er, mod)
    ans = (ans * 2) % mod
    if n == 0:
        ans = 0
    return ans

def main(n):
    # n controls the scale; generate deterministic (n, k) from n
    # For time complexity experiments, let k grow with n
    k = n * 2 + 3
    result = original_logic(n, k)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)