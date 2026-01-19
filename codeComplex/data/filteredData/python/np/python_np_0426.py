def main(n):
    # n 表示矩阵的行数，列数 m 由 n 映射得到且 m <= 10
    if n <= 0:
        return

    # 将 n 映射到列数 m（保持与原算法一致，最多 10 列）
    m = max(1, min(10, n))

    # 构造一个确定性的 n x m 矩阵 arrmv
    # 使用简单算术生成，完全确定：arrmv[i][j] = (i * 7 + j * 13 + 3) % (10**9 + 7)
    mod_val = 10**9 + 7
    arrmv = [[(i * 7 + j * 13 + 3) % mod_val for j in range(m)] for i in range(n)]

    x = 0
    y = int(1e9 + 1)
    sucls = [0, 0]

    tols = []
    mstr = ""

    powls = [int(pow(2, i)) for i in range(10)]
    twodarray = [0 for _ in range(257)]
    while x + 1 < y:
        mid = x + (y - x) // 2
        for idx in range(len(twodarray)):
            twodarray[idx] = 0
        tols.clear()
        for topidx, eletop in enumerate(arrmv):
            tmp = 0
            for idx, ele in enumerate(eletop):
                if ele >= mid:
                    tmp += powls[idx]
            if not twodarray[tmp]:
                twodarray[tmp] = 1
                tols.append((tmp, topidx))
        sz = len(tols)
        suc = 0
        no = int(pow(2, m))
        for i in range(sz):
            for j in range(i, sz):
                if tols[i][0] | tols[j][0] == no - 1:
                    sucls[0], sucls[1] = tols[i][1], tols[j][1]
                    suc = 1
                    break
            if suc:
                break
        if suc:
            x = mid
        else:
            y = mid

    print(sucls[0] + 1, sucls[1] + 1)


if __name__ == "__main__":
    # 示例调用：将 n 视为输入规模（矩阵行数）
    main(1000)