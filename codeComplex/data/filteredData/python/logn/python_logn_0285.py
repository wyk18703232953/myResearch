MOD = 1000000007

def pow2(n):
    if n == 0:
        return 1
    t = pow2(n // 2) % MOD
    m = (t * t) % MOD
    if n % 2 == 1:
        m = (m * 2) % MOD
    return m

def main(n):
    # 根据规模 n 生成测试数据：
    # 这里假设：
    #   x = n
    #   k = n
    # 可根据需要更改为其他生成规则
    x = n
    k = n

    if x == 0:
        print(0)
        return

    t = pow2(k) * (2 * x - 1) % MOD
    print((t + 1) % MOD)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)