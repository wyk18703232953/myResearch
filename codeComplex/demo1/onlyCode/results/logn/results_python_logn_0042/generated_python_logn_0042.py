def main(n: int):
    # 根据 n 生成测试数据
    # 这里将 n 映射为区间 [l, r]，r = n，l = max(1, r - n + 1) = 1（当 n>=1）
    # 为了更通用一点，这里设定：
    # l = max(0, n // 2 - 5), r = l + n
    # 这样可以覆盖更一般的区间情况
    l = max(0, n // 2 - 5)
    r = l + n

    masks = []
    for i in range(64, -1, -1):
        if (1 << i) > r:
            continue
        masks.append(1 << i)
        x, y = 0, 0
        for k in masks:
            if x < y:
                x += k
            else:
                y += k
        for j in range(64, -1, -1):
            if ((x >> j) & 1) or ((y >> j) & 1):
                continue
            if x + (1 << j) <= r:
                x += (1 << j)
            if y + (1 << j) <= r:
                y += (1 << j)
        if min(x, y) < l or max(x, y) > r:
            masks.pop()
    print(sum(masks))


if __name__ == "__main__":
    # 示例：用 n = 100 运行
    main(100)