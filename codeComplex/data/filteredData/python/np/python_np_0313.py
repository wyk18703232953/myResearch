def main(n: int):
    # 根据规模 n 生成测试数据：这里简单设定 k = n
    k = n

    same = [0] * (k + 1)
    diff = [0] * (k + 1)
    mod = 998244353
    if k >= 1:
        same[1] = 2
    if k > 1:
        diff[2] = 2

    for _ in range(n - 1):
        newsame = [0] * (k + 1)
        newdiff = [0] * (k + 1)
        for i in range(1, k + 1):
            newsame[i] = (same[i] + same[i - 1] + 2 * diff[i]) % mod
        for i in range(2, k + 1):
            newdiff[i] = (2 * same[i - 1] + diff[i] + diff[i - 2]) % mod
        same = newsame
        diff = newdiff

    # print((same[-1] + diff[-1]) % mod)
    pass
if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)