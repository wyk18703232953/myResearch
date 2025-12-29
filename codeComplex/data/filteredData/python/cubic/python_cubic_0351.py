import bisect
import random

def get_prime(n):
    res = []
    for i in range(2, n):
        is_prime = True
        for x in res:
            if i % x == 0:
                is_prime = False
                break
        if is_prime:
            res.append(i)
    return res

cache = {}
prime = get_prime(3162)

def get_mask(num):
    key = num
    if key in cache:
        return cache[key]
    dv = []
    tmp = num
    for p in prime:
        if p * p > tmp:
            break
        c = 0
        while tmp % p == 0:
            c += 1
            tmp //= p
        if c % 2 == 1:
            dv.append(p)
    # if tmp > 1, it is a prime factor with odd exponent 1
    if tmp > 1:
        dv.append(tmp)
        tmp = 1
    for x in dv:
        tmp *= x
    cache[key] = tmp
    return tmp

def get_left(n, k, lst):
    last_in = {}
    s = []
    res = []
    for i in range(n):
        group = get_mask(lst[i])
        if group in last_in:
            bisect.insort(s, last_in[group] + 1)
        last_in[group] = i
        if len(s) <= k + 1:
            res.append(s[::-1])
        else:
            m = len(s)
            res.append(s[m - 1:m - k - 2:-1])
    return res

def get_dp(n, k, lst):
    res = []
    left = get_left(n, k, lst)
    for i in range(n):
        arr = left[i]
        row = [n] * (k + 1)
        for j in range(k + 1):
            for g in range(j + 1):
                if g >= len(arr):
                    row[j] = 1
                else:
                    index = arr[g] - 1
                    jindex = j - g
                    row[j] = min(res[index][jindex] + 1, row[j])
        res.append(row)
    return res

def f(n, k, lst):
    dp = get_dp(n, k, lst)
    return dp[n - 1][k]

def main(n):
    """
    n: problem size, used to generate one random test instance.
    We generate:
        - n: length of array
        - k: number of allowed operations in [0, min(20, n)]
        - lst: array of length n with values in [1, 10^6]
    The function prints the answer for this single test.
    """
    # bound k to avoid very heavy DP for large n
    k = random.randint(0, min(20, n - 1 if n > 0 else 0)) if n > 0 else 0
    # generate test data
    if n <= 0:
        print(0)
        return
    # values chosen so factorization is still reasonable
    lst = [random.randint(1, 10**6) for _ in range(n)]
    ans = f(n, k, lst)
    print(ans)

if __name__ == "__main__":
    # example: run with n = 100
    main(100)