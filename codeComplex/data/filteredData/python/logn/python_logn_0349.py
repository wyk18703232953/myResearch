MOD = 1000000007

def modpow(x, p):
    result = 1
    x %= MOD
    while p > 0:
        if p & 1:
            result = (result * x) % MOD
        p >>= 1
        x = (x * x) % MOD
    return result

def main(n):
    # 根据规模 n 生成测试数据：
    # 原程序需要两个整数 n, k，这里用 n 作为原来的 n，
    # 并构造一个与规模相关的 k，例如 k = n（也可以根据需要更改生成规则）
    k = n

    k += 1
    if n == 0:
        ans = 0
    else:
        ans = (((modpow(2, k)) * (n % MOD)) % MOD - (modpow(2, k - 1) - 1) % MOD) % MOD

    print(ans)

if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的值进行测试
    main(10)