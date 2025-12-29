import random

def main(n):
    # 生成测试数据：n 给定，随机生成一个模数 mod（大于 n 且为奇数，尽量避免太小）
    # 实际使用时可直接修改这一行固定 mod
    mod = 10**9 + 7

    le = 405

    def pow_mod(x, y):
        ans = 1
        while y > 0:
            if y % 2 == 1:
                ans = (ans * x) % mod
            x = (x * x) % mod
            y //= 2
        return ans

    def inv(x):
        return pow_mod(x, mod - 2)

    # 预计算阶乘及其逆元
    M = [1]  # i! mod
    mul = 1
    for i in range(1, le):
        mul = (mul * i) % mod
        M.append(mul)

    MI = [0] * (le - 1) + [inv(M[le - 1])]  # (i!)^{-1} mod
    for i in range(le - 2, -1, -1):
        MI[i] = MI[i + 1] * (i + 1) % mod

    def C(x, y):
        if y < 0 or y > x:
            return 0
        elif x > le:  # O(min(y, x-y))
            y = min(y, x - y)
            ans = 1
            for i in range(x, x - y, -1):
                ans = (ans * i) % mod
            return (ans * MI[y]) % mod
        else:  # O(1)
            ans = M[x]
            ans = (ans * MI[y]) % mod
            return (ans * MI[x - y]) % mod

    # 2 的幂
    M2 = [1]
    for _ in range(n + 5):
        M2.append((M2[-1] * 2) % mod)

    # 组合数表
    CO = [[0] * (n + 5) for _ in range(n + 5)]
    for i in range(n + 5):
        for j in range(n + 5):
            CO[i][j] = C(i, j)

    # DP
    # D[已考虑个数][其中手动 ON 的个数] = 方案数（最右为自动 ON 的情况）
    D = [[0] * (n + 1) for _ in range(n + 2)]
    D[0][0] = 1

    for i in range(n + 2):
        for j in range(i // 2, min(n + 1, i + 1)):
            for k in range(1, min(n + 1, n - i + 1, n - j + 1)):
                ind0 = i + k + 1
                ind1 = j + k
                if ind0 <= n + 1 and ind1 <= n:
                    D[ind0][ind1] += D[i][j] * CO[j + k][k] * M2[k - 1]
                    D[ind0][ind1] %= mod

    ans = sum(D[-1]) % mod
    print(ans)
    return ans


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行调整
    main(10)