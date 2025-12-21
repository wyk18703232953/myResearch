def main(n):
    mod = 1000000007
    x = n
    k = n
    if x == 0:
        return 0
    a = pow(2, k, mod) % mod
    b = (2 * a) % mod
    return (((((x % mod) * (b % mod)) % mod) - (a % mod) + 1) + mod) % mod

if __name__ == "__main__":
    print(main(10))