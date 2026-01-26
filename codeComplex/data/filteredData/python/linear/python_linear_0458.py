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

def main(n):
    # Interpret n as the length of the parentheses string s.
    # Construct a deterministic test case:
    # n, k = length of s, and k is an even number <= n.
    if n < 2:
        # For very small n, no valid k, just print empty and return
        # print("")
        pass
        return

    # Make k the largest even <= n
    k = n if n % 2 == 0 else n - 1

    # Deterministically construct s of length n with balanced-like pattern:
    # First half '(' and second half ')'
    half = n // 2
    s = "(" * half + ")" * (n - half)

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
    # print(lts(ans))
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n to scale input size
    main(10)