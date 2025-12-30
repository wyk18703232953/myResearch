def main(n):
    # 根据 n 生成测试数据，这里示例为让 k 取一个与 n 相关的值
    # 你可以按需要修改生成方式
    k = max(0, n - 2)

    grid = [['.'] * n for _ in range(4)]
    if k % 2 == 0:
        for i in range(k // 2):
            if 1 + i < n:  # 防止越界
                grid[1][1 + i] = '#'
            if 1 + i < n:
                grid[2][1 + i] = '#'
    else:
        m = n // 2
        if k > n - 2:
            for i in range(1, n - 1):
                grid[1][i] = '#'
            for i in range(1, (k - n + 2) // 2 + 1):
                if m + i < n:
                    grid[2][m + i] = '#'
                if m - i >= 0:
                    grid[2][m - i] = '#'
        else:
            if 0 <= m < n:
                grid[1][m] = '#'
            if k > 1:
                for i in range(1, k // 2 + 1):
                    if m - i >= 0:
                        grid[1][m - i] = '#'
                    if m + i < n:
                        grid[1][m + i] = '#'

    print('YES')
    for row in grid:
        print(''.join(row))


if __name__ == "__main__":
    # 示例调用，可根据需要修改或在外部调用 main(n)
    main(10)