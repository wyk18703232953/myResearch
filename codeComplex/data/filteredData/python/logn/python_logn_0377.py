MOD = int(1e9) + 7

def fast_power(x, y):
    res = 1
    x %= MOD
    while y > 0:
        if y % 2 == 1:
            res = (res * x) % MOD
        x = (x * x) % MOD
        y >>= 1
    return res

def main(n):
    # 根据规模 n 生成测试数据
    # 示例：x = n, k = n^2
    x = n % MOD
    k = (n * n) % (10**18)  # 保持 k 较大但不过分

    if x == 0:
        ans = 0

    else:
        a = fast_power(2, k)
        b = (2 * x - 1) % MOD
        c = (a * b) % MOD + 1
        ans = c % MOD

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例调用：可按需修改 n
    main(10)