MOD = 10**9 + 7

def solve(x, k):
    if x == 0:
        return 0
    a = x * pow(2, k + 1, MOD) % MOD
    b = (a - pow(2, k, MOD) + 1) % MOD
    return b

def main(n):
    # 生成规模为 n 的测试数据
    # 这里构造 x, k 与 n 相关，使得数据随 n 变化
    x = n % MOD
    k = n  # 也可以使用例如 k = n // 2 等其他方式

    ans = solve(x, k)
    print(ans)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)