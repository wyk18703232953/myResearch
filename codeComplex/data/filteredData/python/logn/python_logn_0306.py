def binary_exp(x, n, prime):
    if n == 0:
        return 1
    elif n == 1:
        return x % prime

    else:
        temp = binary_exp(x, n // 2, prime)
        temp = (temp * temp) % prime
        if n % 2 == 0:
            return temp

        else:
            return ((x % prime) * temp) % prime


def core_logic(x, k):
    MOD = 1000000007
    if x == 0:
        return 0
    val1 = binary_exp(2, k + 1, MOD)
    val2 = binary_exp(2, k, MOD)
    val1 %= MOD
    val2 %= MOD
    ans = ((val1 * (x % MOD)) % MOD - (val2 - 1) % MOD) % MOD
    return ans


def main(n):
    # 映射：n -> (x, k)
    # 设 k = n，x = n^2 + 1，保证确定性且规模随 n 增大
    k = n
    x = n * n + 1
    result = core_logic(x, k)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)