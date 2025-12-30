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

# for positive integers only
def nCr(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n - r)

mod = int(1e9) + 7

def main(n):
    """
    n: 规模，用于控制测试数据大小。
    这里根据 n 生成 (n, k)：
      - n 本身作为方程中的 n
      - k 在 [1, n^2] 范围内随机生成（至少为 1）
    然后执行原逻辑：
        n, k = nninp()
        nos = floor(sqrt(2*k))
        找 i 使得 (i*(i+1))//2 - k + i == n
        输出 (i*(i+1))//2 - k
    """
    # 生成测试数据
    N = max(1, n)
    K = random.randint(1, max(1, N * N))

    # 对应原始代码中的 n, k
    n_val = N
    k_val = K

    nos = math.floor(math.sqrt(2 * k_val))
    # 上界保持原程序的写法
    for i in range(nos, 12309123):
        if (i * (i + 1)) // 2 - k_val + i == n_val:
            print((i * (i + 1)) // 2 - k_val)
            return

    # 若没有找到解，给出一个可见输出（原代码会一直循环到上界然后结束）
    print(-1)


if __name__ == "__main__":
    # 示例调用：可根据需要修改规模
    main(10)