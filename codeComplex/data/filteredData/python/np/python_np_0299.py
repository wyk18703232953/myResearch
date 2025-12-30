from math import gcd, ceil
import random

def prod(a, mod=10**9+7):
    ans = 1
    for each in a:
        ans = (ans * each) % mod
    return ans

def lcm(a, b):
    return a * b // gcd(a, b)

def binary(x, length=16):
    y = bin(x)[2:]
    return y if len(y) >= length else "0" * (length - len(y)) + y

def main(n):
    # 1. 生成测试数据：长度为 n 的数组 a，元素范围 [1, 10^5]
    MAXV = 10**5
    random.seed(0)
    a = [random.randint(1, MAXV) for _ in range(n)]

    mod = 10**9 + 7

    # 2. 预计算 2 的幂
    twosz = MAXV + 69
    twopow = [1] * twosz
    for i in range(1, twosz):
        twopow[i] = (twopow[i - 1] * 2) % mod

    # 3. 统计每个值出现次数
    SZ = MAXV + 69
    count = [0] * SZ
    for v in a:
        count[v] += 1

    # 4. multiples[i] = 数组中是 i 的倍数的元素个数
    multiples = [0] * SZ
    for i in range(1, MAXV + 1):
        s = 0
        for j in range(i, MAXV + 1, i):
            s += count[j]
        multiples[i] = s

    # 5. 包含-排除计算 gcd_of[i]
    gcd_of = [0] * SZ
    for i in range(MAXV, 0, -1):
        gcd_of[i] = (twopow[multiples[i]] - 1) % mod
        for j in range(2 * i, MAXV + 1, i):
            gcd_of[i] -= gcd_of[j]

    ans = gcd_of[1] % mod
    print(ans)

if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)