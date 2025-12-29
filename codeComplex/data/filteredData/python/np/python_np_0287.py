def main(n):
    mod = 10**9 + 7
    l = 100000

    # 生成测试数据：在 [1, l] 范围内循环取值
    a = [(i % l) + 1 for i in range(n)]

    cnt = [0] * (l + 1)
    for v in a:
        cnt[v] += 1

    pow2 = [1] * (l + 1)
    for i in range(1, l + 1):
        pow2[i] = (pow2[i - 1] * 2) % mod

    ans = pow2[n] - 1
    x = [-1] * (l + 1)

    for i in range(2, l + 1):
        c = cnt[i]
        xi = x[i]
        for j in range(2 * i, l + 1, i):
            c += cnt[j]
            x[j] -= xi
        ans = (ans + xi * (pow2[c] - 1)) % mod

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)