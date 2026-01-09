def main(n):
    # 映射规模参数 n 到原程序的 n, m, k, l
    # 保证确定性且可规模化
    if n < 4:
        N = 4

    else:
        N = n

    # 构造参数
    total_n = N * 3
    m = max(1, N // 2)
    k = N
    l = N // 3

    need = k + l
    if need % m == 0 and need <= total_n:
        # print(need // m)
        pass

    else:
        x = need // m + 1
        if x * m > total_n:
            # print(-1)
            pass

        else:
            # print(x)
            pass
if __name__ == "__main__":
    main(10)