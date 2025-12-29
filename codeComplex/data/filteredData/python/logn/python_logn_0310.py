MOD = 10**9 + 7

def repow(n):
    if n == 1:
        return 2
    if n % 2 == 0:
        return pow(repow(n // 2), 2, MOD)
    else:
        return (2 * pow(repow(n // 2), 2, MOD)) % MOD

def main(n):
    """
    n 用作规模参数，这里我们根据 n 生成一组 (x, k) 测试数据。
    你可以根据实际需求修改数据生成策略。
    当前策略：
      x = n
      k = n^2
    """
    x = n
    k = n * n

    if 0 < k and 0 < x:
        if MOD <= k:
            while MOD <= k:
                k = (k // MOD) + (k % MOD)
        tmp = (2 * x - 1) % MOD
        ans = (tmp * repow(k) + 1) % MOD
    else:
        ans = (2 * x) % MOD

    print(ans)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(10)