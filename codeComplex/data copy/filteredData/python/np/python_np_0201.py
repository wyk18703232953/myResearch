def main(n):
    # 参数生成：n 对应元素个数
    if n < 2:
        print(0)
        return

    # 生成 l, r, d，全部由 n 确定性生成
    # l 至少为 1，r 至少为 l，d 非负
    l = n // 2 + 1
    r = n * (n + 1) // 4 + 3  # 保证不小于 l
    if r < l:
        r = l
    d = max(0, n // 3)

    # 生成长度为 n 的确定性数组 op
    # 示例：op[i] = (i+1)*(i%3+1)
    op = [(i + 1) * ((i % 3) + 1) for i in range(n)]

    c = 0
    # 遍历所有非空非单元素子集（位掩码从 1 到 2^n-1）
    for mask in range(1, 1 << n):
        # 统计子集中元素个数
        k = mask.bit_count()
        if k < 2:
            continue

        s = 0
        maxx = 0
        minn = 1000001

        # 遍历每一位，决定是否选取对应元素
        m = mask
        idx = 0
        while m:
            if m & 1:
                v = op[idx]
                s += v
                if v > maxx:
                    maxx = v
                if v < minn:
                    minn = v
            m >>= 1
            idx += 1

        if l <= s <= r and maxx - minn >= d:
            c += 1

    print(c)


if __name__ == "__main__":
    # 示例调用：可按需修改 n 以调整规模
    main(10)