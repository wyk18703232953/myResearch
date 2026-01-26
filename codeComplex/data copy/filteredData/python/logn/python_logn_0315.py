MOD = 10**9 + 7

def main(n):
    """
    n: 规模，用来生成测试数据 (x, k)
    这里示例生成方式为：
    x = n
    k = n 的比特长度
    """
    x = n
    k = max(0, n.bit_length() - 1)

    y = (2 * x - 1) % MOD
    mult = pow(2, k, MOD)
    if x:
        ans = (y * mult + 1) % MOD

    else:
        ans = 0
    return ans

if __name__ == "__main__":
    # 示例：调用 main(10)
    # print(main(10))
    pass