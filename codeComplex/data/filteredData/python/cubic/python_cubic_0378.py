import random

def main(n):
    # 生成测试数据：给定 n，构造一个模数 mod
    # 要求：mod 为素数且 > n，便于取逆元；这里简单取一个固定的大质数
    mod = 10**9 + 7

    le = 500

    def mod_pow(x, y):
        ans = 1
        x %= mod
        while y > 0:
            if y & 1:
                ans = (ans * x) % mod
            x = (x * x) % mod
            y >>= 1
        return ans

    def inv(x):
        # mod 为素数，使用费马小定理
        return mod_pow(x, mod - 2)

    # 预处理阶乘 (最多只用到 le-1)
    M = [1]
    mul = 1
    for i in range(1, le):
        mul = (mul * i) % mod
        M.append(mul)

    L0 = n // 2 + 3
    L1 = n + 1

    D = [[0 for _ in range(L1)] for _ in range(L0)]
    ND = [[0 for _ in range(L1)] for _ in range(L0)]

    INVS = [0] + [inv(i) for i in range(1, n + 1)]

    D[1][1] = 1
    for z in range(2, n + 1):
        l0 = z // 2 + 3
        l1 = z + 1

        # 清空 ND
        for i in range(l0):
            row = ND[i]
            for j in range(l1):
                row[j] = 0

        # 转移 1：开始一个新段，长度为 1
        for i in range(l0):
            if i >= 1:
                ND[i][1] += D[i - 1][0] * (z - (i - 1))
                ND[i][1] %= mod

        # 转移 2：把所有长度 >=1 的段收缩成长度 0（某种状态聚合）
        for i in range(l0):
            s = 0
            Di = D[i]
            for j in range(1, n + 1):
                s += Di[j]
            ND[i][0] = (ND[i][0] + s) % mod

        # 转移 3：在当前段上继续扩展
        for i in range(l0):
            Di = D[i]
            NDi = ND[i]
            for j in range(2, l1):
                p = Di[j - 1]
                if p == 0:
                    continue
                p *= (z - (i - 1))
                p %= mod
                p *= INVS[j] * 2
                p %= mod
                NDi[j] = (NDi[j] + p) % mod

        # 复制回 D
        for i in range(l0):
            Di = D[i]
            NDi = ND[i]
            for j in range(l1):
                Di[j] = NDi[j]

    ans = 0
    for i in range(L0):
        for j in range(1, L1):
            ans += D[i][j]
            ans %= mod

    print(ans)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(10)