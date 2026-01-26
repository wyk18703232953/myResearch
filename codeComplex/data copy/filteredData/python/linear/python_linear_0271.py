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

# if  number is prime in √n time
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

# for positive integerse only
def nCr(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n - r)

mod = int(1e9) + 7

def generate_tree_edges(n):
    # Construct a deterministic tree of size n (star centered at 1)
    edges = []
    for v in range(2, n + 1):
        edges.append((1, v))
    return edges

def run_core_logic(n, edges):
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

            else:
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
    if n < 1:
        return ""
    if n == 1:
        return "Yes\n0"
    edges = generate_tree_edges(n)
    return run_core_logic(n, edges)

if __name__ == "__main__":
    # Example deterministic runs for timing / scaling
    for size in [5, 10, 100]:
        result = main(size)
        # print(f"n = {size}")
        pass
        # print(result)
        pass
        # print("-----")
        pass