def main(n):
    # In the original program, input structure: two integers x, k
    # Here we map n -> (x, k) deterministically
    # Choose x and k as simple functions of n to scale input size meaningfully
    x = n
    k = n

    if x == 0:
        # print(0)
        pass
        return

    MOD = 10**9 + 7
    ans = (pow(2, k + 1, MOD) * x % MOD - (pow(2, k, MOD) - 1)) % MOD
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)