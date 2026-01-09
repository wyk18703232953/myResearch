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
    root = int(n ** 0.5)
    root += 1
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

import math

def nCr(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n - r)

mod = int(1e9) + 7

def core_algorithm(n, k, s):
    ans = []
    lb = k // 2
    rb = k // 2
    for c in s:
        if lb > 0:
            if c == "(":
                lb -= 1

            else:
                rb -= 1
            ans.append(c)
        elif rb > 0:
            if c == ")":
                ans.append(c)
                rb -= 1
        elif lb == 0 and rb == 0:
            break
    return lts(ans)

def generate_input(n):
    # Define k based on n, ensure k is even and <= length of s.
    # We choose k = 2 * (n // 4) so that k grows with n but k <= n.
    # Also ensure k >= 2 when n >= 2.
    k = 2 * (n // 4)
    if k < 2 and n >= 2:
        k = 2
    if k > n:
        k = n if n % 2 == 0 else n - 1

    # Generate a deterministic parentheses string s of length n
    # Pattern: alternate "(" and ")", then repeat; ensures balanced-like structure.
    chars = []
    for i in range(n):
        if i % 4 in (0, 1):
            chars.append("(")

        else:
            chars.append(")")
    s = ''.join(chars)
    return n, k, s

def main(n):
    n_val, k_val, s_val = generate_input(n)
    result = core_algorithm(n_val, k_val, s_val)
    # print(result)
    pass
if __name__ == "__main__":
    main(20)