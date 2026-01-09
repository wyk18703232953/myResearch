import math

def binary(n):
    return bin(n).replace("0b", "")

def decimal(s):
    return int(s, 2)

def pow2(n):
    p = 0
    while n > 1:
        n //= 2
        p += 1
    return p

def isPrime(n):
    if n == 1:
        return False
    root = int(n ** 0.5) + 1
    for i in range(2, root):
        if n % i == 0:
            return False
    return True

def lts(l):
    return ''.join(map(str, l))

def stl(s):
    return list(s)

def sq(a, target, arr=None):
    if arr is None:
        arr = []
    s = sum(arr)
    if s == target:
        return arr
    if s >= target:
        return None
    for i in range(len(a)):
        n = a[i]
        remaining = a[i + 1:]
        ans = sq(remaining, target, arr + [n])
        if ans:
            return ans
    return None

def SieveOfEratosthenes(n):
    cnt = 0
    prime = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, n + 1):
        if prime[p]:
            cnt += 1
    return cnt

def nCr(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n - r)

mod = int(1e9) + 7

def core_logic(n, k):
    nos = math.floor(math.sqrt(2 * k))
    upper = 12309123
    for i in range(nos, upper):
        if (i * (i + 1)) // 2 - k + i == n:
            return (i * (i + 1)) // 2 - k
    return None

def main(n):
    # Deterministic generation of (n, k) pairs.
    # Here, n is treated as the input scale; we derive a single (n_val, k_val)
    # from it in a deterministic way.
    n_val = n
    # Ensure k is positive and grows with n to exercise the sqrt and loop
    k_val = n * (n + 1) // 4 + 1
    res = core_logic(n_val, k_val)
    # To keep behavior similar to original (which printed then exited),
    # we print the result (or -1 if not found).
    if res is None:
        # print(-1)
        pass

    else:
        # print(res)
        pass
if __name__ == "__main__":
    main(1000)