def binar(a, st, d):
    if st == 0:
        return 1
    elif st == 1:
        return a % d
    return (binar(a * a % d, st // 2, d) * binar(a, st % 2, d)) % d

def main(n):
    MOD = 1000000007
    x = n
    k = n + 5
    if x == 0:
        # print(0)
        pass
        return
    res = ((x * binar(2, k + 1, MOD)) - binar(2, k, MOD) + 1) % MOD
    # print(res)
    pass
if __name__ == "__main__":
    main(10)