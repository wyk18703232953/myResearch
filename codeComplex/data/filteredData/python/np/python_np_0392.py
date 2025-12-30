def main(n):
    # 生成测试数据：n 行，m 列
    import random
    random.seed(0)
    m = max(1, n // 2)  # 简单设定列数与 n 相关
    a = [[random.randint(0, 10**9) for _ in range(m)] for _ in range(n)]

    mi = -1
    ma = 10**9
    ans = []

    while mi < ma:
        mid = (mi + ma + 1) // 2
        masks = {}
        for i in range(n):
            currMask = 0
            for j in range(m):
                if a[i][j] >= mid:
                    currMask |= 1 << j
            masks[currMask] = i

        req = (1 << m) - 1
        possible = 0
        for i_mask in masks:
            for j_mask in masks:
                if i_mask | j_mask == req:
                    possible = 1
                    ans = [masks[i_mask] + 1, masks[j_mask] + 1]
                    break
            if possible:
                break

        if possible:
            mi = mid
        else:
            ma = mid - 1

    print(*ans)


if __name__ == "__main__":
    # 示例调用：可自行修改 n
    main(5)