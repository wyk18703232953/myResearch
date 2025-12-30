import random
import math
from collections import defaultdict

def ncr(n, r, p):  # using Fermat's little theorem
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den, p - 2, p)) % p


def primeFactors(n):
    l = []
    while n % 2 == 0:
        l.append(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            l.append(int(i))
            n = n / i
    if n > 2:
        l.append(n)
    return list(set(l))


def power(x, y, p):
    res = 1
    x = x % p
    if x == 0:
        return 0
    while y > 0:
        if (y & 1) == 1:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res


def prefix_sum(arr):
    r = [0] * (len(arr) + 1)
    for i, el in enumerate(arr):
        r[i + 1] = r[i] + el
    return r


def divideCeil(n, x):
    if n % x == 0:
        return n // x
    return n // x + 1


def main(n):
    """
    n: problem size, used as length of generated array per test case.
    生成测试数据并执行原逻辑，打印答案。
    """
    t = 3  # 生成 3 个测试用例
    print(t)
    for _ in range(t):
        # 生成长度为 n 的数组，每个元素在 [1, 50] 范围内
        # 为了更容易出现答案，值域不取太大
        arr_len = max(4, n)  # 至少 4 个元素才有意义
        l = [random.randint(1, 50) for _ in range(arr_len)]

        print(arr_len)
        print(" ".join(map(str, l)))

        # 原逻辑开始
        l1 = l[:]
        arr = defaultdict(lambda: 0)
        for val in l:
            arr[val] += 1

        keys_for_pairs = []
        greater_than_4_val = 0
        is_greater_than_4 = False

        for key in list(arr.keys()):
            if arr[key] >= 4:
                is_greater_than_4 = True
                greater_than_4_val = key
            if arr[key] >= 2:
                keys_for_pairs.append(key)

        keys_for_pairs.sort()
        m = 10**12
        mi = []

        for i in range(len(keys_for_pairs) - 1):
            a = keys_for_pairs[i]
            b = keys_for_pairs[i + 1]
            val = a / b + b / a
            if val < m:
                m = val
                mi = [a, b]

        if is_greater_than_4:
            print(greater_than_4_val, greater_than_4_val, greater_than_4_val, greater_than_4_val)
        else:
            if mi:
                a, b = mi
                print(a, a, b, b)
            else:
                # 没有任何值出现至少两次，原题这种情况一般不会出现；
                # 这里退化输出前四个元素作为占位。
                print(l[0], l[0], l[1], l[1])


if __name__ == "__main__":
    # 示例调用：规模 n = 10
    main(10)