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

def core_logic(n, m, grid):
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
                    return (i + 1 + (cnt // 2), c - (cnt // 2))
        if cnt % 2 == 1:
            return (i + 1 + cnt // 2, c + 1 - cnt // 2)
    return None

def generate_grid(n, m):
    # Deterministic pattern: alternate rows, within each row pattern depends on (i+j)
    grid = []
    for i in range(n):
        row_chars = []
        for j in range(m):
            # simple deterministic rule: "B" when (i*j + i + j) % 3 == 0 else "W"
            val = (i * j + i + j) % 3
            if val == 0:
                row_chars.append("B")

            else:
                row_chars.append("W")
        grid.append(''.join(row_chars))
    return grid

def main(n):
    # Interpret n as total number of cells ~= n, choose n rows and n cols (n x n grid)
    # To keep it simple and scalable, use n rows and n columns; ensure at least 1
    if n <= 0:
        n_eff = 1

    else:
        n_eff = n
    rows = n_eff
    cols = n_eff
    grid = generate_grid(rows, cols)
    res = core_logic(rows, cols, grid)
    # For complexity experiments we just print the result (or -1 if no position)
    if res is None:
        # print(-1)
        pass

    else:
        # print(res[0], res[1])
        pass
if __name__ == "__main__":
    # example deterministic call for complexity experiments
    main(10)