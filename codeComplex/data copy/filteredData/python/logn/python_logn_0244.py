MOD = 10**9 + 7

def pow2(k):
    if k == 0:
        return 1
    if k == 1:
        return 2
    r = pow2(k // 2)
    r = r * r
    if k % 2 != 0:
        r *= 2
    return r % MOD

def calc(x, k):
    if x == 0:
        return 0
    if k == 0:
        return (2 * x) % MOD
    r = pow2(k) * (2 * x - 1) + 1
    return r % MOD

def main(n):
    # 根据规模 n 生成测试数据
    # 这里示例：令 x = n, k = n
    x = n
    k = n
    result = calc(x, k)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)