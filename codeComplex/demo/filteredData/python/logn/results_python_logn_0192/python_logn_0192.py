def bin_func(num, s):
    i = 9 * num * 11
    for _ in range(100):
        add = 0
        a = str(i)
        for k in range(10):
            add += a.count(str(k)) * k
        if i - add >= s:
            return i
        i += 1
    return -1


def solve_single(n, s):
    i = 0
    j = 10 ** 30
    while i < j:
        m = (i + j) // 2
        if bin_func(m, s) == -1:
            i = m + 1

        else:
            j = m
    return max(0, n - bin_func(i, s) + 1)


def main(n):
    # 将 n 作为测试规模：构造 n 组 (n_i, s_i) 测试
    # 第 t 组：n_t = t * n + 1, s_t = (t * 7 + n) % (10**6 + 3)
    total = 0
    for t in range(1, n + 1):
        nt = t * n + 1
        st = (t * 7 + n) % (10**6 + 3)
        total += solve_single(nt, st)
    # print(total)
    pass
if __name__ == "__main__":
    main(10)