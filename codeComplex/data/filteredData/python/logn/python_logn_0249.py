MOD = 10**9 + 7

def solve(x, k):
    if x == 0:
        return 0
    return (x * pow(2, k + 1, MOD) - pow(2, k, MOD) + 1) % MOD

def main(n):
    # 根据规模 n 生成测试数据：
    # 这里简单设定 x = n, k = n（也可按需修改生成规则）
    x = n
    k = n

    ans = solve(x, k)
    print(ans)

if __name__ == "__main__":
    # 示例：调用 main，规模自定义
    main(10)