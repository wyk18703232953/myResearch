MOD = 1000000007

def f(k):
    res = 1
    a = 2
    while k:
        if k % 2 == 1:
            res *= a
            k -= 1
        else:
            a *= a
            k //= 2
        res %= MOD
        a %= MOD
    return res

def main(n):
    # 根据规模 n 生成测试数据：
    # 这里假设 n 为原程序中的 n，同时生成一个与 n 同规模的 k
    # 你可以根据需要修改生成规则
    k = n  # 简单示例：令 k = n

    if n == 0:
        print(0)
    elif k == 0:
        print((n * 2) % MOD)
    else:
        first = (2 * n - 1) % MOD
        first *= f(k)
        first = (first + 1) % MOD
        print(first)

if __name__ == "__main__":
    # 示例：调用 main，使用某个规模 n
    main(10)