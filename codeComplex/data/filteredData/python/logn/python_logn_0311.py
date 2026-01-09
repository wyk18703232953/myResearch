MOD = 1000000007

def fast_power(base, power):
    result = 1
    while power > 0:
        if power % 2 == 1:
            result = (result * base) % MOD
        power //= 2
        base = (base * base) % MOD
    return result

def main(n):
    # 根据 n 生成测试数据，这里简单设定：
    # x = n, k = n（可按需要修改为其他函数关系）
    x = n
    k = n

    if x == 0 or k == 0:
        ans = (x * 2) % MOD

    else:
        d = ((x * 4) - 1) - (x * 2)
        ans = ((x * 2) + (d * (fast_power(2, k) - 1))) % MOD

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：用 n = 10 作为规模运行
    main(10)