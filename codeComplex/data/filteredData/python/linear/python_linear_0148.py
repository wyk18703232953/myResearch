def main(n):
    # 映射：n 为列表长度，k 为一个与 n 相关的确定性值
    if n <= 0:
        print(0)
        return

    k = n + 1  # 保证 k > 0，且随 n 确定性变化

    # 确定性生成长度为 n 的整数列表
    lst = [(i * 2 + 3) % (k + 5) for i in range(n)]

    s = sum(lst)
    s2 = 0
    m = 0
    for i in range(n - 1):
        s2 += lst[i]
        s -= lst[i]
        cur = (s2 % k) + (s % k)
        if cur > m:
            m = cur
    print(m)


if __name__ == "__main__":
    # 示例：使用 n = 10 进行一次规模为 10 的实验
    main(10)