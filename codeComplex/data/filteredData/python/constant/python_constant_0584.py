def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True

def mhd(a, b, x, y):
    return abs(a - x) + abs(b - y)

def main(n):
    a = 1 + (n // 3)
    b = n - (n // 4)
    if mhd(a, b, 1, 1) <= mhd(a, b, n, n):
        # print('White')
        pass

    else:
        # print('Black')
        pass
if __name__ == "__main__":
    main(10)