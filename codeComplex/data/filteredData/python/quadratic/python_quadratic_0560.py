def main(n):
    # 将单个 n 映射为原程序中的 (n, m)
    # 这里选择 n_rows = n, n_cols = n，保证规模随 n 增长
    n_rows = n
    n_cols = n

    r = []
    rappend = r.append
    for i in range(1, (n_rows >> 1) + 1):
        for j in range(1, n_cols + 1):
            rappend(str(i) + ' ' + str(j))
            rappend(str(n_rows + 1 - i) + ' ' + str(n_cols + 1 - j))

    if n_rows & 1:
        for i in range(1, (n_cols >> 1) + 1):
            rappend(str((n_rows + 1) >> 1) + ' ' + str(i))
            rappend(str((n_rows + 1) >> 1) + ' ' + str(n_cols + 1 - i))
        if n_cols & 1:
            rappend(str((n_rows + 1) >> 1) + ' ' + str((n_cols + 1) >> 1))

    print('\n'.join(r))


if __name__ == "__main__":
    main(5)