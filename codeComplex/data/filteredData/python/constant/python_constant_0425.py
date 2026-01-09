import math

# decimal to binary
def binary(n):
    return bin(n).replace("0b", "")

# binary to decimal
def decimal(s):
    return int(s, 2)

# power of a number base 2
def pow2(n):
    p = 0
    while n > 1:
        n //= 2
        p += 1
    return p

# if number is prime in √n time
def isPrime(n):
    if n == 1:
        return False
    root = int(n ** 0.5) + 1
    for i in range(2, root):
        if n % i == 0:
            return False
    return True

# list to string ,no spaces
def lts(l):
    return ''.join(map(str, l))

# String to list
def stl(s):
    return list(s)

# Returns list of numbers with a particular sum
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

# Sieve for prime numbers in a range
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

# for positive integers only
def nCr(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n - r)

mod = int(1e9) + 7

def core_logic(n, k):
    if k >= 2 * n:
        return 0
    elif k <= n:
        if k % 2 == 1:
            return k // 2

        else:
            return k // 2 - 1

    else:
        if k % 2 == 1:
            return k // 2 - (k - n) + 1

        else:
            return k // 2 - (k - n)

def main(n):
    # Interpret n as the problem size, and deterministically generate (n, k)
    # Ensure n >= 1
    if n <= 0:
        n_val = 1

    else:
        n_val = n

    # Generate k as a deterministic function of n to exercise all branches:
    # Let k cycle through [1, 2*n_val] as n grows
    k_val = (3 * n_val) % (2 * n_val + 1)
    if k_val == 0:
        k_val = 1

    result = core_logic(n_val, k_val)
    # print(result)
    pass
if __name__ == "__main__":
    # Example deterministic call for experimental purpose
    main(10)