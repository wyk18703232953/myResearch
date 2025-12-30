# 将原程序改为无 input()，由 main(n, M) 驱动。
# 根据 n 生成测试数据的含义：由调用者传入 n，M；程序内部不再依赖外部输入。

combdic = {}

def fastfrac(a, b, M):
    # a / b (mod M)，利用费马小定理：b^(M-2) 为逆元（假设 M 为素数）
    numb = pow(b, M - 2, M)
    return (a % M) * (numb % M) % M

def comb(p, q, M):
    # 组合数 C(q, p)，带记忆化
    if p == 1:
        return q % M
    if (p, q) in combdic:
        return combdic[(p, q)]
    output = (comb(p - 1, q - 1, M) * q) % M
    output = fastfrac(output, p, M)
    combdic[(p, q)] = output
    return output

def main(n, M=10**9+7):
    # 清空全局缓存
    global combdic
    combdic = {}

    # dp[i][j] 含义同原程序
    dp = [[0 for _ in range(n // 2 + 3)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = (1 << (i - 1)) % M
        for j in range(1, n + 1):
            if 2 * j + 1 > i:
                break
            for k in range(2, i):
                if 2 * j - 1 > i - k:
                    break
                dp[i][j] += (dp[i - k][j - 1] * dp[k - 1][0]) % M * comb(k - 1, i - j, M)
                dp[i][j] %= M

    ans = 0
    for j in range(n):
        if 2 * j + 1 > n:
            break
        ans += dp[n][j]
        ans %= M

    print(ans)
    return ans

# 示例：可以在本文件直接调用 main 进行测试
if __name__ == "__main__":
    # 根据需要修改 n, M 作为“测试数据”
    main(10, 10**9 + 7)