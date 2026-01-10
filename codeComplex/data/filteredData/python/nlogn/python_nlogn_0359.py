import math as mt

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


def core_algorithm(a):
    n = len(a)
    d = {}
    for i in range(n):
        d[a[i]] = i
    found = [-1, -1, -1]
    found2 = [-1, -1]
    for i in range(n):
        c = 1
        while c < (1 << 31):
            if a[i] - c in d.keys() and a[i] + c in d.keys():
                found[0] = a[i] - c
                found[1] = a[i]
                found[2] = a[i] + c
            if a[i] - c in d.keys():
                found2 = [a[i], a[i] - c]
            if a[i] + c in d.keys():
                found2 = [a[i], a[i] + c]
            c *= 2
    outputs = []
    if found[0] == found[1]:
        if found2[0] == found2[1]:
            outputs.append("1")
            outputs.append(str(a[0]))
        else:
            outputs.append("2")
            outputs.append(" ".join(map(str, found2)))
    else:
        outputs.append("3")
        outputs.append(" ".join(map(str, found)))
    return "\n".join(outputs)


def generate_input_array(n):
    if n <= 0:
        return []
    # Deterministic construction: mix linear and modular patterns
    a = [(i * 3 + (i // 2)) % (4 * n + 7) for i in range(n)]
    # Ensure some structure for potential arithmetic (power-of-two) differences
    for i in range(1, min(n, 20)):
        a[i] = a[0] + (1 << (i - 1))
    return a


def main(n):
    a = generate_input_array(n)
    result = core_algorithm(a)
    print(result)


if __name__ == "__main__":
    main(10)