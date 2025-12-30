import math
import random

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

# for positive integerse only
def nCr(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n - r)

mod = int(1e9) + 7

def main(n):
    # 生成测试数据：
    # 对于给定规模 n，生成一组 (n, k)
    # 让 k 在 [1, 2n] 范围内随机取值（保证覆盖各个分支）
    if n <= 0:
        return

    k = random.randint(1, 2 * n)

    # 原始核心逻辑
    if k >= 2 * n:
        ans = 0
    elif k <= n:
        if k % 2 == 1:
            ans = k // 2
        else:
            ans = k // 2 - 1
    else:
        if k % 2 == 1:
            ans = k // 2 - (k - n) + 1
        else:
            ans = k // 2 - (k - n)

    print(ans)

# 示例：需要时可以这样调用
# if __name__ == "__main__":
#     main(10)