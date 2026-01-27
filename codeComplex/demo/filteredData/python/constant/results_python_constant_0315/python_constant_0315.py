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

def core_logic(a):
    ans = 0
    for i in range(14):
        temp = a.copy()
        nos = temp[i]
        temp[i] = 0
        for j in range(i + 1, 14):
            temp[j] += 1
            nos -= 1
        for j in range(14):
            temp[j] += nos // 14
        nos = nos % 14
        j = 0
        while nos != 0 and j < 14:
            temp[j] += 1
            nos -= 1
            j += 1
        ans1 = 0
        for c in temp:
            if c % 2 == 0:
                ans1 += c
        ans = max(ans, ans1)
    return ans

def generate_input_array(n):
    base = n if n > 0 else 1
    return [((i + 1) * base) % 1000003 for i in range(14)]

def main(n):
    a = generate_input_array(n)
    result = core_logic(a)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)