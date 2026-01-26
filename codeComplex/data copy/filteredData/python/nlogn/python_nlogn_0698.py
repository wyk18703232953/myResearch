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


def main(n):
    # Deterministically generate the array a of length n
    # Example pattern: non-decreasing with some repetitions
    # a[i] = i // 2 ensures sorted and has duplicates
    a = [i // 2 for i in range(n)]
    a.sort()

    same = 0
    ind = -1
    poss = 1
    for i in range(1, n):
        same += (a[i] == a[i - 1])
        if a[i] == a[i - 1]:
            ind = i - 1
            if a[i] == 0:
                poss = 0
    if same > 1 or poss == 0:
        # print('cslnb')
        pass

    else:
        if ind > 0:
            if a[ind] - a[ind - 1] == 1:
                # print('cslnb')
                pass
                return
        c = 0
        for i in range(n):
            c += a[i] - i
        if c % 2:
            # print('sjfnb')
            pass

        else:
            # print('cslnb')
            pass
    return


if __name__ == "__main__":
    main(10)