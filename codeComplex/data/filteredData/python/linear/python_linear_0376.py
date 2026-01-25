def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

def SieveOfEratosthenes(n):
    prime = []
    primes = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if primes[p]:
            prime.append(p)
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return prime

def factors(n):
    fac = []
    while n % 2 == 0:
        fac.append(2)
        n = n // 2
    i = 3
    while i <= int(n ** 0.5) + 1:
        while n % i == 0:
            fac.append(i)
            n = n // i
        i += 2
    if n > 1:
        fac.append(n)
    return fac

def generate_string(n):
    if n <= 0:
        return ""
    chars = []
    for i in range(n):
        r = i % 3
        if r == 0:
            chars.append('1')
        elif r == 1:
            chars.append('2')
        else:
            chars.append('0')
    return "".join(chars)

def core_logic(a):
    b = a.count('1')
    a = a.replace('1', '')
    c = a.find('2')
    if c == -1:
        a = a + '1' * b
    else:
        a = a[:c] + '1' * b + a[c:]
    return a

def main(n):
    s = generate_string(n)
    result = core_logic(s)
    print(result)

if __name__ == "__main__":
    main(10)