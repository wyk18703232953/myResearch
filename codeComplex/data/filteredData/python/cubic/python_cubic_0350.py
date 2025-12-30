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

prime = get_prime(3162)

def get_mask(num):
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
    """
    n: 规模参数，用于生成测试数据。
       这里设定：
       - 测试组数 T = 1
       - 每组长度 len(lst) = n
       - k = min(20, n-1)（保证 k < n 且不过大）
       - 每个元素在 [1, 10^6] 之间随机生成
    """
    if n < 2:
        return  # 规模太小，不做测试

    T = 1
    results = []
    for _ in range(T):
        size = n
        k = min(20, size - 1)
        lst = [random.randint(1, 10**6) for _ in range(size)]
        ans = f(size, k, lst)
        results.append((size, k, ans))

    # 输出结果，可根据需要调整格式
    for size, k, ans in results:
        print(size, k, ans)

if __name__ == "__main__":
    # 示例：以 n = 100 作为规模运行
    main(100)