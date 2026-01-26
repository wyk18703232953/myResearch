MOD = 1000000007

def fast_pow(n: int) -> int:
    if n > 0:
        if n % 2 == 0:
            x = fast_pow(n // 2) % MOD
            return (x * x) % MOD

        else:
            return (fast_pow(n - 1) * 2) % MOD

    else:
        return 1

def main(n: int):
    """
    n: 规模参数，用于生成测试数据。
       这里约定：
       - n 用作原程序中的 k
       - 原程序中的 n 固定设为 n+1，用以构造非零场景
    """
    # 生成测试数据：
    # 将原来的 (n, k) 构造为 (n_data, k_data)
    # 保证 n_data != 0，避免总是输出 0
    n_data = n + 1     # 原程序中的 n
    k_data = n         # 原程序中的 k

    if n_data == 0:
        # print(0)
        pass

    else:
        result = (fast_pow(k_data) * (2 * n_data - 1) + 1) % MOD
        # print(result)
        pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的值进行测试
    main(10)