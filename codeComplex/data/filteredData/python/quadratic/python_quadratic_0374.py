def norm(x):
    return (x % 998244353 + 998244353) % 998244353


def core(n, k):
    dp1 = [0]
    dp2 = [0]

    for i in range(n):
        l = [1]
        cur = 0
        for j in range(n + 1):
            cur += l[j]
            if j > i:
                cur -= l[j - i - 1]
            cur = norm(cur)
            l.append(cur)
        dp1.append(l[n])
        dp2.append(norm(dp1[i + 1] - dp1[i]))

    ans = 0
    for i in range(n + 1):
        for j in range(n + 1):
            if i * j < k:
                ans = norm(ans + dp2[i] * dp2[j])

    ans = norm(ans * 2)
    return ans


def main(n):
    # 输入结构：单组测试，两个整数 n, k
    # 规模映射：参数 n 即为原程序中的 n，k 也由 n 决定
    # 确定性生成 k，这里选取 k = n * (n // 2)
    k = n * (n // 2)
    result = core(n, k)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例：以 n = 200 作为规模
    main(200)