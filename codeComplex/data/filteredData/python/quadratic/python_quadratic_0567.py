def main(n):
    # 将单个规模参数 n 映射为原程序的 n, m
    # 这里设定 m = n，保证规模随 n 线性增长且结构合理
    orig_n = n
    orig_m = n

    r = []
    rappend = r.append
    for i in range(1, (orig_n >> 1) + 1):
        for j in range(1, orig_m + 1):
            rappend(str(i) + ' ' + str(j))
            rappend(str(orig_n + 1 - i) + ' ' + str(orig_m + 1 - j))
    if orig_n & 1:
        for i in range(1, (orig_m >> 1) + 1):
            rappend(str((orig_n + 1) >> 1) + ' ' + str(i))
            rappend(str((orig_n + 1) >> 1) + ' ' + str(orig_m + 1 - i))
        if orig_m & 1:
            rappend(str((orig_n + 1) >> 1) + ' ' + str((orig_m + 1) >> 1))
    # print('\n'.join(r))
    pass
if __name__ == "__main__":
    main(5)