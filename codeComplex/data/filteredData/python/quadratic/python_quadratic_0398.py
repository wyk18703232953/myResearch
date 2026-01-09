import math

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
        if prime[p] is True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, n + 1):
        if prime[p]:
            cnt += 1
    return cnt

def nCr(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n - r)

mod = int(1e9) + 7

def main(n):
    # Interpret n as both the number of rows and columns of the grid
    # Generate a deterministic n x n grid of 'W' and 'B'
    # Pattern: cell (i,j) is 'B' if (i + j) % 3 == 0 else 'W'
    m = n
    ans = None  # to store the found coordinates or None
    cnt = 0
    f = 0

    for i in range(n):
        # generate row string deterministically
        row_chars = []
        for j in range(m):
            if (i + j) % 3 == 0:
                row_chars.append("B")

            else:
                row_chars.append("W")
        s = ''.join(row_chars)

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
                    ans = (i + 1 + (cnt // 2), c - (cnt // 2))
                    # simulate exit by ending all processing
                    # print(ans[0], ans[1])
                    pass
                    return
        # after processing row
        if cnt % 2 == 1:
            # c is the last index from the loop if it ran at least once
            # if m>0, c is defined; when m==0, loop didn't run and cnt==0
            if m > 0:
                ans = (i + 1 + cnt // 2, c + 1 - cnt // 2)
                # print(ans[0], ans[1])
                pass
                return

    # If no early exit occurred, print something deterministic
    # For compatibility we can print -1 -1 if no coordinates found
    # print(-1, -1)
    pass
if __name__ == "__main__":
    # Example call for time complexity experiments
    main(1000)