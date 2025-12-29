def f_pow(a, n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n % 2 == 0:
        return f_pow(a * a, n // 2)
    else:
        return a * f_pow(a, n - 1)


def get_c(n):
    if n > 68:
        return int(1e40)
    return (f_pow(4, n) - 4) // 12


def get_cc(n):
    if n > 51:
        return int(1e30)
    return (f_pow(4, n) - 4) // 12


def ans(n, k):
    side = n - 1
    way = 4
    cnt_all = get_c(n + 1)
    c = 2
    op = 1
    while True:
        if k < op or side < 0:
            break
        way_blocks = way - 1
        if get_cc(side - 1) > k:
            return side
        per_block = get_cc(side + 1)
        kk = k - op
        if cnt_all - way_blocks * per_block - op >= kk:
            return side

        side -= 1
        op += (1 << c) - 1
        c += 1
        way *= 2
    return -1


def main(n):
    """
    n: 规模参数，用于控制自动生成的测试数据。
       这里约定：
       - 生成 t = n 组测试；
       - 对于第 i 组（1 <= i <= n）:
            N_i = i + 1
            K_i = i - 1
    """
    t = n
    for i in range(1, t + 1):
        N = i + 1          # 简单生成：N 从 2,3,4,...,n+1
        K = i - 1          # K 从 0,1,2,...,n-1
        a = ans(N, K)
        if a == -1:
            print("NO")
        else:
            print("YES {}".format(a))


if __name__ == "__main__":
    # 示例：以 n=5 运行主函数
    main(5)