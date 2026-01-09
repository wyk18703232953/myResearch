def power(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if (y & 1) == 1:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res

def main(n):
    mod = (10**9) + 7
    r = n
    k = n
    if r == 0:
        # print(0)
        pass
        return
    # print((((power(2, k + 1, mod) * (r % mod)) % mod) - power(2, k, mod) + 1) % mod)
    pass
if __name__ == "__main__":
    main(10)