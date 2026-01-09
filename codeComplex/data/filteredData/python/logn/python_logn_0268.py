def get2k(k, base):
    f = 2
    b = 1
    r = 1
    while k >= b:
        if k & b > 0:
            r = r * f % base
        b *= 2
        f = f * f % base
    return r

def core(x, k, base):
    if x == 0:
        return 0
    t2k = get2k(k, base)
    r = x * t2k * 2 - t2k + 1
    r = r % base
    return r

def main(n):
    base = 10**9 + 7
    x = n
    k = n // 2
    result = core(x, k, base)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)