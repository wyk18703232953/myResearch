def main(n):
    # 确定性生成长度为 n 的数组 a
    # 例如：a[i] = (i * 3 + 1) % (n + 7) + 1，保证为正整数且有一定分布
    a = [((i * 3 + 1) % (n + 7)) + 1 for i in range(n)]

    a.sort()
    sum1 = 0
    rem = sum(a)
    i = len(a) - 1
    c = 0
    while sum1 <= rem and i >= 0:
        sum1 += a[i]
        rem = sum(a) - sum1
        i -= 1
        c += 1
    # print(c)
    pass
if __name__ == "__main__":
    # 示例：以 n = 10 作为输入规模运行
    main(10)