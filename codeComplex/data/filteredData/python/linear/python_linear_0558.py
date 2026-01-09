def main(n):
    # 映射输入结构：
    # 原程序：第一行 n, k；第二行 n 个整数 A
    # 这里：n 为规模，k 取一个与 n 有关的确定性值，A 为长度为 n 的确定性序列

    if n <= 0:
        return

    # 确定性生成 k，使得 2^k 有一定规模，防止过大或过小
    # 例如：k 为 1 到 20 之间的循环递增
    k = (n % 20) + 1

    ans = [0] * n
    lul = 2 ** k - 1

    # 确定性生成数组 A：例如 A[i] = (i * 3 + 7) % (2^k)
    # 保证与 k 有关，同时完全确定
    A = [(i * 3 + 7) & lul for i in range(n)]

    ans[0] = A[0]
    for j in range(1, n):
        ans[j] = ans[j - 1] ^ A[j]

    d = dict()
    for j in range(n):
        v = ans[j]
        if v in d:
            d[v] += 1

        else:
            d[v] = 1

    total_ans = 0

    def huy(x):
        return x * (x - 1) // 2

    for j in d:
        now = d[j]
        xor = lul ^ j
        cur = now
        if xor in d:
            now2 = d[xor]
            cur += now2
            total_ans += huy(cur // 2 + cur % 2)
            total_ans += huy(cur // 2)
            if j == 0:
                total_ans += 2 * (cur // 2)

        else:
            if j == 0 or xor == 0:
                total_ans += 2 * (cur // 2)
            total_ans += 2 * huy(cur // 2 + cur % 2)
            total_ans += 2 * huy(cur // 2)

    result = huy(n + 1) - total_ans // 2
    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n 以进行规模实验
    main(10)