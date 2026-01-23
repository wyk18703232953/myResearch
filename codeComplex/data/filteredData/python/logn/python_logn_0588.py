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

def p(xyz):
    print(xyz)

def p2(a, b):
    print(a, b)

def core_logic(n, k):
    nos = int(math.floor(math.sqrt(2 * k)))
    for i in range(nos, 12309123):
        if (i * (i + 1)) // 2 - k + i == n:
            return (i * (i + 1)) // 2 - k
    return None

def main(n):
    # 输入结构：原程序为单组输入两个整数 n, k
    # 这里将实验规模 n 映射为：
    #   输入中的第一个参数 = n
    #   输入中的第二个参数 k = n^2
    param_n = n
    param_k = n * n
    ans = core_logic(param_n, param_k)
    if ans is not None:
        print(ans)
    else:
        # 若找不到满足条件的 i，为保持确定性，打印一个固定值
        print(-1)

if __name__ == "__main__":
    # 示例调用：可以按需修改 n 的大小做时间复杂度实验
    main(1000)