MOD = 1000000007

def power(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y & 1:
            res = (res * x) % p
        y >>= 1
        x = (x * x) % p
    return res

def solve(d, n):
    if d == 0:
        return 0
    ans = power(2, n + 1, MOD)
    ans1 = power(2, n, MOD)
    return (ans * (d % MOD) % MOD - ans1 + 1) % MOD

def main(n):
    # 根据规模 n 生成测试数据：这里令 d = n
    d = n
    result = solve(d, n)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例运行：可按需修改 n 的值进行测试
    main(10)