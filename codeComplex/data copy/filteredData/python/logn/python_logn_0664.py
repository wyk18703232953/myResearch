import math as mt

p = 10**9 + 7
inv = [0] * 300001
fact = [0] * 300001

def ncr_util():
    inv[0] = inv[1] = 1
    fact[0] = fact[1] = 1
    for i in range(2, 300001):
        inv[i] = (inv[i % p] * (p - p // i)) % p
    for i in range(1, 300001):
        inv[i] = (inv[i - 1] * inv[i]) % p
        fact[i] = (fact[i - 1] * i) % p

def solve(n, k):
    a = 1
    b = 2 * n + 3
    c = n + n ** 2 - 2 * k
    disc = b * b - 4 * a * c
    x1 = b + int(mt.isqrt(disc))
    x2 = b - int(mt.isqrt(disc))
    if x1 % 2 == 0 and x1 // 2 <= n:
        return x1 // 2
    return x2 // 2

def main(n):
    # Deterministic generation of n, k based on input size n
    # Let problem-scale n be the same n, and k be a deterministic function of n
    n_val = n
    k_val = (n * (n + 1)) // 4
    # Optionally call ncr_util to keep its cost in experiments if desired
    ncr_util()
    ans = solve(n_val, k_val)
    # print(ans)
    pass
if __name__ == "__main__":
    main(1000)