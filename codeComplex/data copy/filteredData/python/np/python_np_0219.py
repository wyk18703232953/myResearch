def main(n):
    # 映射 n 为原程序中的 n，其他参数由 n 确定性生成
    if n <= 0:
        print(0)
        return

    # 生成 c 列表，长度为 n
    c = [(i * 2 + 1) for i in range(n)]

    # 生成 l, r, x，保证与规模 n 有关且确定性
    total_sum = sum(c)
    l = total_sum // 4
    r = (total_sum * 3) // 4
    if l > r:
        l, r = r, l
    x = max(1, n // 3)

    res = 0
    for mask in range(1 << n):
        Bit = []
        for j in range(n):
            if mask & (1 << j):
                Bit.append(c[j])
        if len(Bit) >= 2 and l <= sum(Bit) <= r and (max(Bit) - min(Bit) >= x):
            res += 1
    print(res)


if __name__ == "__main__":
    main(10)