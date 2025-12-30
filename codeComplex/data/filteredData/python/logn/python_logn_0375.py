mod = 1000000007
import math
import random

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

def main(n):
    # 根据规模 n 生成测试数据：
    # 原程序需要 n, k，这里让 k 与 n 同阶，例如 k 在 [1, 2n+1] 范围内
    if n < 0:
        n = 0
    # 保证 k >= 1，避免除以 0 对应的 powm(2,k,mod) 的逆元不存在问题
    k = random.randint(1, 2 * n + 1 if n > 0 else 10)

    ans = (powm(4, k, mod) * n) % mod
    r = powm(2, k, mod)
    r = (powm(r, 2, mod) - r) % mod
    w = modDivide(r, 2, mod)
    ans = (ans - w) % mod  # 保证非负
    er = powm(2, k, mod)
    ans = modDivide(ans, er, mod)
    ans = (ans * 2) % mod
    if n == 0:
        ans = 0
    print(ans)

if __name__ == "__main__":
    # 示例：可以在这里指定规模 n
    main(10)