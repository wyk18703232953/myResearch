def main(n):
    # 确定性生成 k，保证 0 <= k <= 2*(n-2)（题目原约束）
    if n < 3:
        k = 0

    else:
        k = (n * 3) % (2 * (n - 2) + 1)

    grid = [['.'] * n for _ in range(4)]
    if k % 2 == 0:
        for i in range(k // 2):
            if 1 + i < n - 1:
                grid[1][1 + i], grid[2][1 + i] = '#', '#'

    else:
        m = n // 2
        if k > n - 2:
            for i in range(1, n - 1):
                grid[1][i] = '#'
            for i in range(1, (k - n + 2) // 2 + 1):
                if 0 <= m + i < n and 0 <= m - i < n:
                    grid[2][m + i], grid[2][m - i] = '#', '#'

        else:
            if 0 <= m < n:
                grid[1][m] = '#'
            if k > 1:
                for i in range(1, k // 2 + 1):
                    if 0 <= m - i < n and 0 <= m + i < n:
                        grid[1][m - i], grid[1][m + i] = '#', '#'

    # print('YES')
    pass
    for row in grid:
        # print(''.join(row))
        pass
if __name__ == "__main__":
    main(10)