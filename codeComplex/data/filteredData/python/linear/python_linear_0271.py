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

def generate_tree_edges(n):
    """生成一个随机树的 n-1 条边（节点编号 1..n）"""
    edges = []
    for v in range(2, n + 1):
        u = random.randint(1, v - 1)
        edges.append((u, v))
    return edges

def solve(n, edges):
    d = {}
    for u, v in edges:
        d.setdefault(u, []).append(v)
        d.setdefault(v, []).append(u)

    if not d:
        print("No")
        return

    node = next(iter(d))  # 初始取一个存在的节点
    for key in d:
        if len(d[key]) > len(d[node]):
            node = key

    ans = []
    visited = [0] * n
    visited[node - 1] = 1

    for c in d[node]:
        while True:
            visited[c - 1] = 1
            if len(d[c]) == 1:
                ans.append([node, c])
                break
            moved = False
            for child in d[c]:
                if visited[child - 1] != 1:
                    c = child
                    moved = True
                    break
            if not moved:
                break

    if sum(visited) == n:
        print("Yes")
        print(len(ans))
        for c in ans:
            print(*c)
    else:
        print("No")

def main(n):
    # 1. 生成规模为 n 的测试数据（一棵树）
    edges = generate_tree_edges(n)

    # 2. 调用原逻辑
    solve(n, edges)

if __name__ == "__main__":
    # 示例：运行 main(5)
    main(5)