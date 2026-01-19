def main(n):
    # 映射 n 为 (行数, 列数)
    # 保证 m 至少为 1 且不要太大
    m = max(1, min(20, n if n > 0 else 1))
    rows = max(1, n)

    # 确定性生成矩阵 l，大小 rows x m
    # 元素构造：l[i][j] = i * m + j
    l = [[i * m + j for j in range(m)] for i in range(rows)]

    left = 0
    right = 10**9 + 1
    ans = (1, 1)

    while left < right:
        mid = (left + right) // 2
        dicta = {}
        for i in range(rows):
            mask = 0
            for j in range(m):
                mask <<= 1
                if l[i][j] >= mid:
                    mask += 1
            dicta[mask] = i

        ok = False
        for i_mask in dicta:
            for j_mask in dicta:
                if i_mask | j_mask == (1 << m) - 1:
                    ok = True
                    ans = (dicta[i_mask] + 1, dicta[j_mask] + 1)
                    break
            if ok:
                break

        if ok:
            left = mid + 1
        else:
            right = mid

    print(*ans)


if __name__ == "__main__":
    main(10)