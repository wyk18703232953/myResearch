MOD = int(1e9 + 9)

def fast_power(x, y):
    res = 1
    while y > 0:
        if y % 2 == 1:
            res = res * x % MOD
        x = x * x % MOD
        y //= 2
    return res

def solve(n, m, k):
    x = max(0, m - n // k * (k - 1) - n % k)
    z = (m - x * k) % MOD
    res = fast_power(2, x + 1)
    res = (res - 2) % MOD * k % MOD
    res = (res + z) % MOD
    return res

def main(n):
    # 根据规模 n 生成测试数据，这里简单设定：
    # 1 <= k <= n，且 m 不超过 n
    if n < 1:
        return None
    k = max(1, n // 2)
    m = min(n, 2 * k)  # 保证 m 合理且与 n, k 有一定关系
    return solve(n, m, k)

if __name__ == "__main__":
    # 示例：调用 main，规模自行设定
    result = main(10)
    print(result)