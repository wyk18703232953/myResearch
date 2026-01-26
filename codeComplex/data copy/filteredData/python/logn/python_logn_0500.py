def main(n):
    # 原程序：k 为输入的正整数，且 0 < k <= 1e12
    # 这里将 n 直接映射为 k，并做同样的合法性约束裁剪
    if n <= 0:
        k = 1
    elif n > 10**12:
        k = 10**12

    else:
        k = n

    lim_init = 9
    lim = 9
    decimal = 9
    c = 0

    while True:
        c += 1
        if k <= lim:
            diff = lim - k
            pos = diff % c
            diff = diff // c
            diff = decimal - diff
            s = ''.join(list(reversed(str(diff))))
            # 为保持与原程序行为一致，只打印对应字符
            # print(s[pos])
            pass
            break

        else:
            decimal = int(str(lim_init) * (c + 1))
            lim += int(str(lim_init) + '0' * c) * (c + 1)


if __name__ == "__main__":
    # 示例：调用 main(100) 作为规模为 100 的实验
    main(100)