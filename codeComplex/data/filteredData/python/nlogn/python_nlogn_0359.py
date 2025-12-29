import random

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
    # 根据规模 n 生成测试数据：
    # 生成 n 个互不相同的整数，范围可调
    # 为了更易产生满足条件的解，构造部分为等差/等比结构，再打乱
    base = random.randint(-10**6, 10**6)
    step = random.choice([1, 2, 4, 8])
    a = []
    used = set()
    for i in range(n):
        val = base + i * step
        if val in used:
            val = base + i * step + random.randint(1, 10**6)
        a.append(val)
        used.add(val)
    random.shuffle(a)

    d = {}
    for i in range(n):
        d[a[i]] = i

    found = [-1, -1, -1]
    found2 = [-1, -1]

    for i in range(n):
        c = 1
        while c < (1 << 31):
            if a[i] - c in d and a[i] + c in d:
                found[0] = a[i] - c
                found[1] = a[i]
                found[2] = a[i] + c
            if a[i] - c in d:
                found2 = [a[i], a[i] - c]
            if a[i] + c in d:
                found2 = [a[i], a[i] + c]
            c *= 2

    if found[0] == found[1]:
        if found2[0] == found2[1]:
            print(1)
            print(a[0])
        else:
            print(2)
            print(*found2)
    else:
        print(3)
        print(*found)


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)