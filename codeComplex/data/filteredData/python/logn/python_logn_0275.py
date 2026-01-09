mod = 1000000007

def somaPa(nSteps):
    if nSteps == 0:
        return 0
    # 该函数在原程序中未被使用，保留以保持结构一致
    return (1 + nSteps) * nSteps // 2

def diminui(step):
    return (pow(2, step, mod) - 2) % mod

def main(n):
    """
    按规模 n 生成一组测试数据 (x, k)，并执行原逻辑。
    这里设定：
    - x 在 [0, n] 范围内
    - k 在 [0, n] 范围内
    可根据需要修改生成规则。
    """
    # 简单的确定性测试数据生成方式（不使用随机数）
    x = n % (mod - 1)           # 避免非常大，但保持随 n 变化
    k = n                       # 将规模 n 直接作为 k

    if x == 0:
        # print(0)
        pass
        return

    pot = pow(2, k + 1, mod)
    inv = pow(2, mod - 2, mod)

    big = (x * pot) % mod
    small = (big - diminui(k + 1)) % mod

    ans = (((big + small) % mod) * inv) % mod
    # print(int(ans))
    pass
if __name__ == "__main__":
    # 示例：使用 n = 10 作为规模
    main(10)