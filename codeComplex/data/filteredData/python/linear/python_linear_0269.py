def binary(n):
    return (bin(n).replace("0b", ""))

def decimal(s):
    return (int(s, 2))

def pow2(n):
    p = 0
    while n > 1:
        n //= 2
        p += 1
    return p

def isPrime(n):
    if n == 1:
        return False

    else:
        root = int(n ** 0.5)
        root += 1
        for i in range(2, root):
            if n % i == 0:
                return False
        return True

def lts(l):
    s = ''.join(map(str, l))
    return s

def stl(s):
    l = list(s)
    return l

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

def deep(node, d, visited):
    visited[node - 1] = 1
    if len(d[node]) == 1:
        return node
    for c in d[node]:
        if visited[c - 1] != 1:
            return deep(c, d, visited)

def build_deterministic_tree(n):
    d = {}
    if n == 1:
        d[1] = []
        return d
    for i in range(2, n + 1):
        u = i
        v = i // 2
        d.setdefault(u, []).append(v)
        d.setdefault(v, []).append(u)
    return d

def core_algorithm(n, d):
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
            progressed = False
            for child in d[c]:
                if visited[child - 1] != 1:
                    c = child
                    progressed = True
                    break
            if not progressed:
                break
    if sum(visited) == n:
        output_lines = []
        output_lines.append("Yes")
        output_lines.append(str(len(ans)))
        for c in ans:
            output_lines.append(f"{c[0]} {c[1]}")
        return "\n".join(output_lines)

    else:
        return "No"

def main(n):
    if n <= 0:
        n = 1
    d = build_deterministic_tree(n)
    result = core_algorithm(n, d)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)