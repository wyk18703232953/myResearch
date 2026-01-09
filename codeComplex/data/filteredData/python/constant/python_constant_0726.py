def main(n):
    # 映射：将 n 作为原程序中的 k 使用
    k = n
    # 修正：如果不合法，映射到一个确定的合法值（例如 1）
    if not isinstance(k, int) or k <= 0 or k > 10**12:
        k = 1

    lim_init = lim = decimal = 9
    c = 0
    while True:
        c += 1
        if k <= lim:
            diff = lim - k
            pos = diff % c
            diff = diff // c
            diff = decimal - diff
            # print(''.join(list(reversed(str(diff))))[pos])
            pass
            break

        else:
            decimal = int(str(lim_init) * (c + 1))
            lim += int(str(lim_init) + '0' * c) * (c + 1)


if __name__ == "__main__":
    # 示例：使用一个确定的 n 调用 main，用于时间复杂度实验
    main(1000)