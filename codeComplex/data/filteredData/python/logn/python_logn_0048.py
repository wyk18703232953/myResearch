def main(n):
    # n 作为输入规模，这里构造两个整数 l, r
    # 确保 l <= r，规模随 n 线性变化
    l = n
    r = 2 * n + 5

    r_bin = bin(r)[2:]
    l_bin = bin(l)[2:]

    r_bin_rev = r_bin[::-1]
    l_bin_rev = l_bin[::-1]

    if l_bin_rev == r_bin_rev:
        # print(0)
        pass

    else:
        if len(l_bin_rev) < len(r_bin_rev):
            l_bin_rev += '0' * (len(r_bin_rev) - len(l_bin_rev))

        p = -1
        for i in range(len(r_bin_rev)):
            if r_bin_rev[i] != l_bin_rev[i]:
                p = i

        if p == -1:
            # print(0)
            pass
            return

        a = '1' * p + '0'
        b = '0' * p + '1'

        # print(int(a, 2) ^ int(b, 2))
        pass
if __name__ == "__main__":
    main(10)