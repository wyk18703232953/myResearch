def main(n):
    MOD = 1000000007
    x = n
    k = n
    if x != 0:
        return ((pow(2, k, MOD) * ((2 * x - 1) % MOD)) % MOD + 1) % MOD
    else:
        return 0

if __name__ == "__main__":
    print(main(10))