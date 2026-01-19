def main(n):
    # 映射 n 为矩阵规模：n = 行数 = 列数
    if n <= 0:
        return
    rows = n
    cols = n

    # 确定性生成矩阵 a，元素值适当分布在一个范围内
    # a[i][j] = (i * 131 + j * 17) % (10**9)
    a = [[(i * 131 + j * 17) % (10**9) for j in range(cols)] for i in range(rows)]

    left = 0
    right = 10**9 + 1
    ans = (0, 0)
    while left < right:
        mid = (left + right) // 2
        masks = {}
        for i in range(rows):
            mask = 0
            for val in a[i]:
                mask <<= 1
                if val >= mid:
                    mask += 1
            masks[mask] = i
        ok = False
        full_mask = (1 << cols) - 1
        for m1 in masks:
            if ok:
                break
            for m2 in masks:
                if m1 | m2 == full_mask:
                    ok = True
                    ans = (masks[m1] + 1, masks[m2] + 1)
                    break
        if ok:
            left = mid + 1
        else:
            right = mid
    print(ans[0], ans[1])


if __name__ == "__main__":
    main(5)