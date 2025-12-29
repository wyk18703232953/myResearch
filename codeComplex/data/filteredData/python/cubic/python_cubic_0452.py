import math
import random

# 保留原工具函数（如需可用）
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

def primeFactors(n):
    l = []
    while n % 2 == 0:
        l.append(2)
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            l.append(i)
            n = n / i
    if n > 2:
        l.append(int(n))
    return l

def isPrime(n):
    if n == 1:
        return False
    root = int(n ** 0.5) + 1
    for i in range(2, root):
        if n % i == 0:
            return False
    return True

def maxPrimeFactors(n):
    maxPrime = -1
    while n % 2 == 0:
        maxPrime = 2
        n >>= 1
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            maxPrime = i
            n = n / i
    if n > 2:
        maxPrime = n
    return int(maxPrime)

def countcon(s, i):
    c = 0
    ch = s[i]
    for i in range(i, len(s)):
        if s[i] == ch:
            c += 1
        else:
            break
    return c

def lis(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    maximum = 0
    for i in range(n):
        maximum = max(maximum, dp[i])
    return maximum

def isSubSequence(str1, str2):
    m = len(str1)
    n = len(str2)
    j = 0
    i = 0
    while j < m and i < n:
        if str1[j] == str2[i]:
            j += 1
        i += 1
    return j == m

def maxfac(n):
    root = int(n ** 0.5)
    for i in range(2, root + 1):
        if n % i == 0:
            return n // i
    return n

def p2(n):
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c

def seive(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, n + 1):
        if primes[i]:
            for j in range(i + i, n + 1, i):
                primes[j] = False
    p = []
    for i in range(0, n + 1):
        if primes[i]:
            p.append(i)
    return p

def ncr(n, r, p):
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den, p - 2, p)) % p

def denofactinverse(n, m):
    fac = 1
    for i in range(1, n + 1):
        fac = (fac * i) % m
    return pow(fac, m - 2, m)

def numofact(n, m):
    fac = 1
    for i in range(1, n + 1):
        fac = (fac * i) % m
    return fac

def sod(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


# ===== 原题核心逻辑改写为可参数化 main(n) =====

def main(n):
    """
    n 作为规模参数：
    - 使用 n 作为网格的行数
    - 列数 m = n 或其他与 n 相关的值
    - 步数参数 k = 2 * n（保证偶数，方便原逻辑）
    - 随机生成边权 hor, ver 作为测试数据
    """
    # 可根据需要调整：例如 m = n 或 m = n+1 等
    m = n
    # 保证 k 为偶数；原题要求如果 k 为奇数则全输出 -1
    # 这里取和规模相关的一个值，比如 2 * n
    k = 2 * n

    # 随机测试数据生成（权值范围可自行调节）
    max_weight = 10
    random.seed(0)

    # hor: n 行，每行 m-1 条水平边（i,j) -> (i,j+1) 的代价
    hor = [[random.randint(1, max_weight) for _ in range(m - 1)] for _ in range(n)]
    # ver: n-1 行，每行 m 条垂直边 (i,j) -> (i+1,j) 的代价
    ver = [[random.randint(1, max_weight) for _ in range(m)] for _ in range(n - 1)]

    # 定义递归/DP所需的变量在闭包外
    inF = 10 ** 20
    half_k = k // 2

    # dp[steps][x][y] = 从 (x,y) 出发走 steps 步到任意点的最小花费
    dp = [[[-1] * m for _ in range(n)] for __ in range(half_k + 1)]

    # 为了与原代码一致，这里沿用 getVal 与 rec 的写法
    def getVal(x, y, sx, sy):
        # (x,y) 与 (sx,sy) 必为相邻；返回边权
        if x < 0 or y < 0 or x >= n or y >= m:
            return inF
        if sx < 0 or sy < 0 or sx >= n or sy >= m:
            return inF

        # 同一行：水平边
        if sx == x:
            # 水平边在 hor[x][min(y, sy)] 上
            j = min(y, sy)
            # j 范围 0..m-2
            if j < 0 or j >= m - 1:
                return inF
            return hor[x][j]
        else:
            # 垂直边在 ver[min(x, sx)][y] 上
            i = min(x, sx)
            if i < 0 or i >= n - 1:
                return inF
            return ver[i][y]

    def rec(steps, x, y):
        # 越界
        if x < 0 or y < 0 or x >= n or y >= m:
            return inF
        if steps == 0:
            dp[steps][x][y] = 0
            return 0
        if dp[steps][x][y] != -1:
            return dp[steps][x][y]

        # 从 (x,y) 走一步到四个方向，再用 steps-1 步
        val1 = rec(steps - 1, x - 1, y) + getVal(x - 1, y, x, y)
        val2 = rec(steps - 1, x + 1, y) + getVal(x + 1, y, x, y)
        val3 = rec(steps - 1, x, y + 1) + getVal(x, y + 1, x, y)
        val4 = rec(steps - 1, x, y - 1) + getVal(x, y - 1, x, y)
        dp[steps][x][y] = min(val1, val2, val3, val4)
        return dp[steps][x][y]

    # 输出结果矩阵：每个点走 k 步回到任意点的最小代价（原题是 2*rec(half_k, i, j)）
    # 这里直接打印到标准输出
    if k % 2 == 1:
        for i in range(n):
            print(" ".join(["-1"] * m))
    else:
        for i in range(n):
            row = []
            for j in range(m):
                ans = rec(half_k, i, j)
                if ans >= inF:
                    row.append("-1")
                else:
                    row.append(str(2 * ans))
            print(" ".join(row))


# 示例：当本文件作为脚本运行时，用一个默认规模测试
if __name__ == "__main__":
    # 可根据需要修改默认 n
    main(3)