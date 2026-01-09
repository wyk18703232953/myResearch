MOD = 1000000007

def powr(n, N):
    temp = 1
    while N > 0:
        if N % 2 != 0:
            temp = (temp * n) % MOD
        n = (n * n) % MOD
        N //= 2
    return temp % MOD

def MODI(a, b):
    return powr(a, b) % MOD

def main(n):
    # 根据规模 n 生成测试数据
    # 这里将 k = n，x = n+1 作为示例测试数据生成逻辑
    x = n + 1
    k = n

    if x == 0:
        ans = 0

    else:
        t1 = powr(2, k + 1) % MOD
        t1 = (t1 * x) % MOD
        t2 = powr(2, k) % MOD
        t2 = (t2 - 1) % MOD
        ans = (t1 - t2) % MOD

    # print(ans)
    pass
    return ans

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)