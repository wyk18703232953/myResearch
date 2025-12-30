def isPoss(threshold, arrs, nvals):
    masks = set()
    midx = {}
    for pos, arr in enumerate(arrs):
        mask = 0
        for i in range(nvals):
            if arr[i] >= threshold:
                mask |= 1 << i
        midx[mask] = pos + 1
        masks.add(mask)

    full_mask = (1 << nvals) - 1
    for m1 in masks:
        for m2 in masks:
            if (m1 | m2) == full_mask:
                return midx[m1], midx[m2]

    return -1, -1


def main(n):
    """
    n: 控制规模的参数，用于生成测试数据
       这里约定：
       - nvals = min(5, max(1, n))   属性数量上限为 5
       - narr  = max(2, 2 * nvals)   数组个数不少于 2
    """
    import random

    # 根据 n 生成测试数据（可按需要调整生成策略）
    nvals = min(5, max(1, n))
    narr = max(2, 2 * nvals)

    # 生成随机测试数据：数值在 [0, 10^9] 区间内
    MAX_VAL = 10**9
    random.seed(0)
    arrs = [
        [random.randint(0, MAX_VAL) for _ in range(nvals)]
        for _ in range(narr)
    ]

    # 二分查找最大阈值
    mn = -1
    mx = MAX_VAL + 1
    while mn < mx - 1:
        mid = (mn + mx) // 2
        a, b = isPoss(mid, arrs, nvals)
        if a != -1:
            mn = mid
        else:
            mx = mid - 1

    # 在 mn 和 mn+1 上做最后确认，输出满足的两个下标
    for delta in range(1, -1, -1):
        a, b = isPoss(mn + delta, arrs, nvals)
        if a != -1:
            print(a, b)
            break


if __name__ == "__main__":
    # 示例：调用 main，规模参数可根据需要修改
    main(3)