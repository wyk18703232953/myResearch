def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return (a * b) / gcd(a, b)


mod = int(1e9) + 7


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


def core_algorithm(n, m, a):
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
    return ans


def main(n):
    if n <= 0:
        return 0
    m = n // 2 if n % 2 == 0 else (n + 1) // 2
    # generate a as a permutation-like sequence containing m exactly once
    # deterministic construction: rotate range(1, n+1) by 1, then place m at position n//3
    base = list(range(1, n + 1))
    a = base[1:] + base[:1]
    pos = n // 3
    if pos >= n:
        pos = n - 1
    # ensure m is in the array and unique
    if m in a:
        a[a.index(m)] = a[pos]
    a[pos] = m
    result = core_algorithm(n, m, a)
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(10)