def main(n):
    # 根据规模 n 生成测试数据：
    # 这里约定：x = n，k = n（可根据需要自行修改生成规则）
    x = n
    k = n

    if x == 0:
        # print('0')
        pass
        return

    mod = 1000000007

    def pow_mod(a, b):
        if b < 2:
            return int(a ** b) % mod
        elif b % 2 == 0:
            return int(pow_mod(a, b // 2) ** 2) % mod

        else:
            return pow_mod(a, b - 1) * a % mod

    twop = pow_mod(2, k)
    high = x * twop
    leafs = twop
    low = high - leafs + 1
    s = (high + 1) * high // 2 - (low - 1 + 1) * (low - 1) // 2
    answer = s * 2 // leafs
    answer %= mod

    # print(answer)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)