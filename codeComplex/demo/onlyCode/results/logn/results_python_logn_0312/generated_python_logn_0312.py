mod = 10 ** 9 + 7

def pow1(n, k):
    if k == 0:
        return 1
    if k == 1:
        return n
    else:
        if k % 2 == 0:
            a = pow1(n, k // 2) % mod
            return a * a % mod
        else:
            return pow1(n, k - 1) % mod * n % mod

def main(n):
    k = n
    if n == 0:
        return 0
    else:
        x = pow1(2, k + 1) % mod
        return ((n * x - pow1(2, k) + 1)) % mod

if __name__ == "__main__":
    print(main(10))