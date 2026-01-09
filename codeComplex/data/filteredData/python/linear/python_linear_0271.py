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

def isPrime(n):
    if n == 1:
        return False
    root = int(n ** 0.5) + 1
    for i in range(2, root):
        if n % i == 0:
            return False
    return True

def lts(l):
    return ''.join(map(str, l))

def stl(s):
    return list(s)

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

import math

def nCr(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n - r)

mod = int(1e9) + 7

def solve_for_tree(n, edges):
    d = {}
    for u, v in edges:
        d.setdefault(u, []).append(v)
        d.setdefault(v, []).append(u)
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
    if sum(visited) == n:
        result = ["Yes", str(len(ans))]
        for c in ans:
            result.append(f"{c[0]} {c[1]}")

    else:
        result = ["No"]
    return "\n".join(result)

def generate_tree_edges(n):
    edges = []
    for i in range(2, n + 1):
        parent = (i // 2)
        if parent < 1:
            parent = 1
        edges.append((parent, i))
    return edges

def main(n):
    if n < 2:
        n_use = 2

    else:
        n_use = n
    edges = generate_tree_edges(n_use)
    output = solve_for_tree(n_use, edges)
    # print(output)
    pass
if __name__ == "__main__":
    main(10)