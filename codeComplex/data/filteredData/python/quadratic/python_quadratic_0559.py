def main(n):
    # 映射规则：n -> (rows, cols) = (n, n)
    rows = n
    cols = n

    r = []
    rappend = r.append
    for i in range(1, (rows >> 1) + 1):
        for j in range(1, cols + 1):
            rappend(str(i) + ' ' + str(j))
            rappend(str(rows + 1 - i) + ' ' + str(cols + 1 - j))

    if rows & 1:
        for i in range(1, (cols >> 1) + 1):
            mid_row = (rows + 1) >> 1
            rappend(str(mid_row) + ' ' + str(i))
            rappend(str(mid_row) + ' ' + str(cols + 1 - i))
        if cols & 1:
            rappend(str((rows + 1) >> 1) + ' ' + str((cols + 1) >> 1))

    # print('\n'.join(r))
    pass
if __name__ == "__main__":
    main(5)