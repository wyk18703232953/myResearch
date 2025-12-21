def binar(a, st, d):
    if st == 0:
        return 1
    elif st == 1:
        return a % d
    return (binar(a * a % d, st // 2, d) * binar(a, st % 2, d)) % d

def main(n):
    x = n
    k = n
    if x == 0:
        return 0
    mod = 1000000007
    res = ((x * binar(2, k + 1, mod)) - binar(2, k, mod) + 1) % mod
    return res

if __name__ == "__main__":
    print(main(10))