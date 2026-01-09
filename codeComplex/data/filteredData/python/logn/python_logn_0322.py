mod = 10**9 + 7

def main(n):
    """
    n 用于生成测试数据：
    若 n 为偶数：x = n, k = n // 2
    若 n 为奇数：x = n // 2, k = n
    可按需要自行调整生成规则。
    """
    if n % 2 == 0:
        x = n
        k = n // 2

    else:
        x = n // 2
        k = n

    if x == 0:
        # print(0)
        pass
    elif k == 0:
        # print((2 * x) % mod)
        pass

    else:
        to = pow(2, k, mod)
        pre = (to * x) % mod
        prev = pow(2, k - 1, mod)
        first = (pre - prev + 1) % mod
        sec = (pre - prev) % mod
        ans = (first + sec) % mod
        # print((ans + mod) % mod)
        pass
if __name__ == "__main__":
    # 示例：调用 main，规模自定义
    main(10)