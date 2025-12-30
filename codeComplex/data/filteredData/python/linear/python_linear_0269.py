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
def sq(a, target, arr=[]):
    s = sum(arr)
    if s == target:
        return arr
    if s >= target:
        return
    for i in range(len(a)):
        n = a[i]
        remaining = a[i + 1:]
        ans = sq(remaining, target, arr + [n])
        if ans:
            return ans

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

def deep(node, d, visited):
    visited[node - 1] = 1
    if len(d[node]) == 1:
        return node
    for c in d[node]:
        if visited[c - 1] != 1:
            return deep(c, d, visited)

def main(n):
    # 1. 生成测试数据：构造一个随机树，n 为结点数量
    # 为了保证是树，依次连接新节点到 [1, i-1] 中的某个节点
    edges = []
    for v in range(2, n + 1):
        u = random.randint(1, v - 1)
        edges.append((u, v))

    # 2. 将测试数据构造成与原程序一致的输入结构
    d = {}
    for u, v in edges:
        d.setdefault(u, []).append(v)
        d.setdefault(v, []).append(u)

    # 3. 按原逻辑运行
    node = 1
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
            for child in d[c]:
                if visited[child - 1] != 1:
                    c = child
                    break
            else:
                # 若没有未访问的 child，说明走到死路，退出
                break

    if sum(visited) == n:
        print("Yes")
        print(len(ans))
        for c in ans:
            print(*c)
    else:
        print("No")

if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)