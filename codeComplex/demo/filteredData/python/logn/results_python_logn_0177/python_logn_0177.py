MOD = 1000000009

def main(n):
    # 根据 n 生成测试数据：
    # 这里定义一个简单的生成方式：
    # m 与 k 都与 n 同阶，且保证 k >= 1
    # 可按需要自行修改生成策略
    if n <= 0:
        return 0

    m = 2 * n          # 示例：m = 2n
    k = max(1, n // 2) # 示例：k = floor(n/2)，但至少为 1

    x = m - (n // k * (k - 1) + (n % k))

    if x <= 0:
        return m % MOD

    # 保持原有的公式逻辑
    return ((m - x) + ((pow(2, x + 1, MOD) + 2 * MOD) - 2) * k - x * (k - 1)) % MOD


if __name__ == "__main__":
    # 示例运行，可根据需要修改 n
    n_example = 10
    result = main(n_example)
    # print(result)
    pass