import sys
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
    n: 控制规模，用来生成测试数据。
       我们生成一个 n x n 的棋盘，每个格子为 'W' 或 'B'。
       然后在该棋盘上运行原有逻辑并打印找到的位置（如果有）。
    """
    # 生成测试数据：n 行，每行 n 个字符 'W' 或 'B'
    # 为了更有可能在中间找到一个奇数长度的 B 段，强制构造一两行有规律的数据
    grid = []

    # 第一行构造：偶数段，不会触发
    if n >= 4:
        # "WWBBWWBB..."
        row = []
        toggle = False
        for _ in range(n):
            row.append('B' if toggle else 'W')
            toggle = not toggle
        grid.append(''.join(row))
    else:
        grid.append(''.join(random.choice(['W', 'B']) for _ in range(n)))

    # 中间行构造：确保有一段奇数长度的 B 段，方便测试
    if n >= 5:
        mid = n // 2
        row = ['W'] * n
        # 在中间放置 3 个连续的 B
        start = max(1, mid - 1)
        end = min(start + 3, n)
        for i in range(start, end):
            row[i] = 'B'
        grid.append(''.join(row))

    # 其余行随机生成
    while len(grid) < n:
        grid.append(''.join(random.choice(['W', 'B']) for _ in range(n)))

    # 在内存中模拟原逻辑
    ans = 0
    cnt = 0
    f = 0

    for i in range(n):
        s = grid[i]
        r = stl(s)
        cnt = 0
        for c in range(len(r)):
            if r[c] == "W" and f == 0:
                pass
            elif r[c] == "B" and f == 0:
                cnt += 1
                f = 1
            elif r[c] == "B" and f == 1:
                cnt += 1
            elif r[c] == "W" and f == 1:
                f = 0
                if cnt % 2 == 1:
                    print(i + 1 + (cnt // 2), c - (cnt // 2))
                    return
        if cnt % 2 == 1:
            # 注意：这里的 c 是循环结束时的最后索引
            print(i + 1 + cnt // 2, c + 1 - cnt // 2)
            return

    # 如果没有找到，打印一个标记结果（如 -1 -1）
    print(-1, -1)


if __name__ == "__main__":
    # 默认给一个规模示例，方便直接运行；评测时可以忽略此处并直接调用 main(n)
    main(8)