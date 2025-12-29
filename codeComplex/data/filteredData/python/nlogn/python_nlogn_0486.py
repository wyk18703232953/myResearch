import math
import operator
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

# for positive integers only
def nCr(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n - r)

mod = int(1e9) + 7

def main(n):
    """
    n: 题目中的 n（需要满足 <= m）。本函数内部根据 n 生成 m 和数组 a。
    生成方式示例：
        m 在 [n, 2n] 之间随机，
        a 为长度为 m 的随机整数数组（值域 1~n）。
    """

    # 生成测试数据
    if n <= 0:
        return

    m = random.randint(n, max(n, 2 * n))  # 保证 m >= n
    a = [random.randint(1, n) for _ in range(m)]

    # 原逻辑开始
    if n > m:
        print(0)
        return

    d = {}
    for c in a:
        d[c] = d.get(c, 0) + 1

    dict1 = dict(sorted(d.items(), key=operator.itemgetter(1)))
    ans = 0
    for i in range(1, 105):
        temp = dict1.copy()
        n1 = n
        for c in temp:
            n1 = n1 - (temp[c] // i)
        if n1 > 0:
            print(i - 1)
            return

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)