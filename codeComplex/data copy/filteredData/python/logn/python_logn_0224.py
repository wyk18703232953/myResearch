def main(n):
    # 这里将原来的 s 也依赖于 n 来生成测试数据
    # 可以根据需要调整生成方式，例如让 s 在 [1, n] 内变化
    s = max(1, n // 2)  # 示例：令 s 为 n 的一半（至少为 1）

    def ver(i):
        t = str(i)
        ans = 0
        for j in t:
            ans += int(j)
        return ans

    l = len(str(s))
    if n < s:
        # print(0)
        pass
        return

    if s + 10 * (l ** 2 + 1) <= n:
        ans = n - s + 1 - 10 * (l ** 2 + 1)
        for i in range(s, s + 10 * (l ** 2 + 1)):
            if s + ver(i) <= i:
                ans += 1

    else:
        ans = 0
        for i in range(s, n + 1):
            if s + ver(i) <= i:
                ans += 1
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：调用 main，n 可按需要修改或由外部测试框架调用
    main(1000000)