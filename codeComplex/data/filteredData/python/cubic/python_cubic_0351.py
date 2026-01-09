import bisect

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
    for p in prime:
        c = 0
        while num % p == 0:
            c += 1
            num = num // p
        if c % 2 == 1:
            dv.append(p)
        if num < p * p:
            break
    for x in dv:
        num *= x
    cache[key] = num
    return num

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
            res.append(s[m-1:m-k-2:-1])
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
    # n is the length of the list; we fix k as a simple function of n
    k = max(0, n // 10)
    # deterministic list generation
    # values are positive integers, varied but deterministic
    lst = [(i * 37) % 1000 + 1 for i in range(1, n + 1)]
    result = f(n, k, lst)
    # print(result)
    pass
if __name__ == "__main__":
    main(1000)