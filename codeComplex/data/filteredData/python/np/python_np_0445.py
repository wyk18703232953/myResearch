def solve(x: int, n: int, m: int, a):
    ans = (-1, -1)
    dp = {}
    for i in range(n):
        temp = 0
        for j in range(m):
            if a[i][j] >= x:
                temp = temp | (1 << j)
        dp[temp] = i
    for aa, bb in dp.items():
        for cc, dd in dp.items():
            if aa | cc == 2 ** m - 1:
                ans = (bb + 1, dd + 1)
                return True, ans
    return False, ans


def main(n):
    # 将 n 映射为矩阵规模：n = 行数 = 列数
    if n <= 0:
        return

    rows = n
    cols = n

    # 确定性生成矩阵 a，元素大小与下标相关
    a = [[(i + 1) * (j + 2) for j in range(cols)] for i in range(rows)]

    l, r = 0, 10 ** 9
    best_ans = (-1, -1)

    while l <= r:
        mid = (l + r) // 2
        ok, cur_ans = solve(mid, rows, cols, a)
        if ok:
            best_ans = cur_ans
            l = mid + 1
        else:
            r = mid - 1

    print(best_ans[0], best_ans[1])


if __name__ == "__main__":
    main(5)