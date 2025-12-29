def main(n):
    # 生成一个与 n 相关的 MOD，用于测试
    # 若需要固定 MOD，可自行替换此行，例如 MOD = 10**9 + 7
    MOD = 10 ** 9 + 7 + n

    # 预处理 Pascal 三角形
    pascal = [[1]]
    for _ in range(500):
        nl = [1]
        for i in range(_):
            nl.append((pascal[-1][i] + pascal[-1][i + 1]) % MOD)
        nl.append(1)
        pascal.append(nl)

    # 兼容原代码接口：保留 mod_mul 名称
    def make_mod_mul(mod=MOD):
        def mod_mul(a, b, c=0):
            # 这里直接使用 Python 的大整数运算和取模
            return (a * b + c) % mod
        return mod_mul

    mod_mul = make_mod_mul()

    def mod_pow(x, y):
        if y == 0:
            return 1
        res = 1
        while y > 1:
            if y & 1 == 1:
                res = mod_mul(res, x)
            x = mod_mul(x, x)
            y >>= 1
        return mod_mul(res, x)

    base = [0] * (n + 1)

    dp = []
    for i in range(n):
        nex = base[:]
        nex[1] = mod_pow(2, i)
        for j in range(i - 1):
            bl = i - j - 1
            assert bl > 0
            mul = mod_pow(2, bl - 1)
            for k in range(n):
                ct = 2 + j - k
                if ct < 0:
                    # 按原逻辑保留断言
                    assert dp[j][k] == 0
                    continue
                mulr = mod_mul(mul, pascal[bl + ct][ct])
                nex[k + 1] += mod_mul(mulr, dp[j][k])
                nex[k + 1] %= MOD
        dp.append(nex)
    ans = sum(dp[-1]) % MOD
    print(ans)
    return ans


if __name__ == "__main__":
    # 示例：运行若干不同规模
    for test_n in [1, 2, 3, 5, 10]:
        main(test_n)