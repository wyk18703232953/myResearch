import random
import math as mt
from collections import Counter

mod = int(1e9) + 7


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return (a * b) / gcd(a, b)


def power(k, n):
    if n == 0:
        return 1
    if n % 2:
        return (power(k, n - 1) * k) % mod
    t = power(k, n // 2)
    return (t * t) % mod


def totalPrimeFactors(n):
    count = 0
    if (n % 2) == 0:
        count += 1
        while (n % 2) == 0:
            n //= 2

    i = 3
    while i * i <= n:
        if (n % i) == 0:
            count += 1
            while (n % i) == 0:
                n //= i
        i += 2
    if n > 2:
        count += 1
    return count


def main(n):
    # 生成测试数据
    # n: 数组长度
    # 数组为 1..n 的随机排列，随机选择一个 m 为其中一个位置的值
    if n <= 0:
        return

    a = list(range(1, n + 1))
    random.shuffle(a)
    m = random.choice(a)

    # 原逻辑开始
    k = a.index(m)
    t = [0]
    for i in range(k - 1, -1, -1):
        z = -1 if a[i] < a[k] else 1
        t.append(t[-1] + z)
    d = {0: 1}
    now = 0
    for i in range(k + 1, n):
        now += -1 if a[i] < a[k] else 1
        if now not in d:
            d[now] = 0
        d[now] += 1

    ans = 0
    for i in t:
        if -i in d:
            ans += d[-i]
        if 1 - i in d:
            ans += d[1 - i]

    print(ans)


if __name__ == "__main__":
    # 示例调用：n 可根据需要调整
    main(10)