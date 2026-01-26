def main(n):
    # 映射：n 为数组长度，k 为一个确定性的函数值
    if n <= 0:
        # print(0)
        pass
        return

    # 确定性生成 k，避免为 0
    k = (n % 5) + 2  # k ∈ [2,6]

    # 确定性生成数组 a，长度为 n
    # 生成一些可被 k 整除和不可被 k 整除的混合数据
    a = [(i * k if i % 3 == 0 else i * 2 + 1) for i in range(1, n + 1)]

    d = {}
    for i in range(n):
        d[a[i]] = 1
    a.sort(reverse=True)
    ans = 0
    for i in range(n):
        if d[a[i]] > 0:
            if a[i] % k == 0:
                x = a[i] // k
                if x in d:
                    d[x] -= 1
            ans += 1
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)