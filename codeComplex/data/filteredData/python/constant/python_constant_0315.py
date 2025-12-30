import math
from collections import OrderedDict
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

def p(xyz): 
    print(xyz)

def p2(a, b): 
    print(a, b)

def generate_test_array(n):
    """
    根据规模 n 生成长度为 14 的数组：
    - 基本长度固定为 14（与原代码一致）
    - n 控制数值范围：元素在 [0, max(1, n)] 间随机
    """
    length = 14
    upper = max(1, n)
    return [random.randint(0, upper) for _ in range(length)]

def solve(a):
    ans = 0
    for i in range(14):
        temp = a.copy()
        nos = temp[i]
        temp[i] = 0

        # 先给右侧一圈各加 1，消耗 nos
        for j in range(i + 1, 14):
            if nos == 0:
                break
            temp[j] += 1
            nos -= 1

        # 平均分配
        add_all = nos // 14
        for j in range(14):
            temp[j] += add_all
        nos %= 14

        # 从 0 开始环形分配剩余 nos
        j = 0
        while nos != 0:
            temp[j] += 1
            nos -= 1
            j += 1

        ans1 = 0
        for c in temp:
            if c % 2 == 0:
                ans1 += c
        ans = max(ans, ans1)
    return ans

def main(n):
    """
    n 为规模参数，只用于控制随机测试数据的数值范围。
    """
    a = generate_test_array(n)
    ans = solve(a)
    p(ans)

if __name__ == "__main__":
    # 示例：使用规模 100 运行一遍
    main(100)