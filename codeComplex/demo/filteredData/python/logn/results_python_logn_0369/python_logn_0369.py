MOD = 1000000007

def power(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y & 1:
            res = (res * x) % p
        y >>= 1
        x = (x * x) % p
    return res

def main(n):
    """
    n 为规模，根据 n 生成测试数据并输出结果。
    这里示例：令 x = n, k = n。
    如需其他生成方式，可按需求修改。
    """
    x = n
    k = n

    if x == 0:
        # print(0)
        pass

    else:
        ans = power(2, k, MOD)
        ans = ans * ((2 * x) - 1)
        ans = ans + 1
        ans = ans % MOD
        # print(ans)
        pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)