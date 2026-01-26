def main(n):
    # 映射：n 作为题目中原始的 n（元素个数）
    # 其余参数从 n 确定性生成
    orig_n = max(1, n)

    # 确定性生成 l, r, x
    # l、r 构造为与 a 的和规模同量级的区间
    # x 为一个固定的差值阈值
    l = orig_n * (orig_n // 2)
    r = orig_n * (orig_n + 1)
    x = max(1, orig_n // 3)

    # 确定性生成数组 a，长度为 orig_n
    # 这里用简单的算术序列构造
    a = [(i * 2 + 1) for i in range(orig_n)]

    count = 0
    for mask in range(1 << orig_n):
        maxc = -1
        minc = -1
        c = 0
        for j in range(orig_n):
            if (mask >> j) & 1 == 1:
                c += a[j]
                if maxc == -1 or a[j] > maxc:
                    maxc = a[j]
                if minc == -1 or a[j] < minc:
                    minc = a[j]
        if maxc != -1 and minc != -1 and l <= c <= r and maxc - minc >= x:
            count += 1

    print(count)


if __name__ == "__main__":
    main(5)