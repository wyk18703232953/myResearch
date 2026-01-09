def main(n):
    mod = 10**9 + 7  # 确定性选择一个常用大质数作为模数

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

    M = [1]
    mul = 1
    for i in range(1, le):
        mul = (mul * i) % mod
        M.append(mul)

    MI = [0] * (le - 1) + [inv(M[le - 1])]
    for i in range(le - 2, -1, -1):
        MI[i] = MI[i + 1] * (i + 1) % mod

    def C(x, y):
        if y < 0 or y > x:
            return 0
        elif x > le:
            y0 = min(y, x - y)
            ans = 1
            for i in range(x, x - y0, -1):
                ans = (ans * i) % mod
            return (ans * MI[y0]) % mod

        else:
            ans = M[x]
            ans = (ans * MI[y]) % mod
            return (ans * MI[x - y]) % mod

    M2 = [1]
    for _ in range(n + 5):
        M2.append((M2[-1] * 2) % mod)

    CO = [[0] * (n + 5) for _ in range(n + 5)]
    for i in range(n + 5):
        for j in range(n + 5):
            CO[i][j] = C(i, j)

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

    result = sum(D[-1]) % mod
    # print(result)
    pass
if __name__ == "__main__":
    # 示例：以 n = 200 作为规模运行一次
    main(200)