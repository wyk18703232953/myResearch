MOD = 1000000007

def mul(x, y, md):
    return x * y % md

def power(x, y, md):
    res = 1
    while y != 0:
        if y & 1:
            res = mul(res, x, md)
        x = mul(x, x, md)
        y >>= 1
    return res

def inv(x, md):
    return power(x, md - 2, md)

def solve(a, k):
    if a == 0:
        return 0
    first = power(2, 2 * k, MOD)
    second = power(2, k, MOD)
    ans = mul(first, 2 * a - 1, MOD) + second
    third = inv(second, MOD)
    ans = mul(ans, third, MOD)
    return ans % MOD

def main(n):
    # 根据规模 n 生成测试数据：
    # 这里简单设定 a = n, k = n，用户可按需修改生成逻辑
    a = n
    k = n
    result = solve(a, k)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例：使用某个固定规模调用 main
    main(10)