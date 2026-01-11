def main(n):
    # 生成确定性参数 a, b，满足 1 <= a < n
    if n < 2:
        a = 1
        b = 1

    else:
        a = max(1, n // 2)
        if a >= n:
            a = n - 1
        b = (a * 3) // 2 if (a * 3) // 2 > 0 else 1

    # 生成长度为 n 的确定性整数列表 alist
    # 使用简单算术构造，保证元素有差异
    alist = [((i * 37 + 13) % (n + 7)) for i in range(n)]

    alist.sort(reverse=True)
    p = alist[a - 1]
    q = alist[a]
    # print(p - q)
    pass
if __name__ == "__main__":
    main(10)