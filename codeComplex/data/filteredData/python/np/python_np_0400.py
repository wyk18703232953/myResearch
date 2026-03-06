def isPoss(n, arrs, nvals):
    masks = set()
    midx = {}
    for pos, arr in enumerate(arrs):
        mask = 0
        for i in range(nvals):
            if arr[i] >= n:
                mask += 1 << i
        midx[mask] = pos + 1
        masks.add(mask)

    full = (1 << nvals) - 1
    for m1 in masks:
        for m2 in masks:
            if m1 | m2 == full:
                return midx[m1], midx[m2]

    return -1, -1


def main(n):
    # 解释输入规模映射：
    # narr: 数组个数，与 n 成比例（至少为 1）
    # nvals: 每个数组的长度，设为一个固定的小常数以控制维度
    if n <= 0:
        return

    nvals = 5  # 固定维度
    narr = max(1, n)

    arrs = []
    # 确定性生成数据：arr[i][j] = (i+1) * (j+2)
    # 数值范围单调随 i,j 增长，便于二分和覆盖情况出现
    for i in range(narr):
        row = []
        base = i + 1
        for j in range(nvals):
            row.append(base * (j + 2))
        arrs.append(row)

    mn = -1
    mx = 10**9 + 1
    while mn < mx - 1:
        mid = (mn + mx) // 2
        a, b = isPoss(mid, arrs, nvals)
        if a != -1:
            mn = mid
        else:
            mx = mid - 1

    res_a, res_b = -1, -1
    for i in range(1, -1, -1):
        a, b = isPoss(mn + i, arrs, nvals)
        if a != -1:
            res_a, res_b = a, b
            break

    # 输出以保持与原程序形式一致
    print(res_a, res_b)


if __name__ == "__main__":
    main(10)