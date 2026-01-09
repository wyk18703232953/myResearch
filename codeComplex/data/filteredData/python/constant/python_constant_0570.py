def main(n):
    # 原程序需要四个整数 n, m, k, l
    # 将参数 n 作为原始 n 的规模，其余三个值按确定性方式生成
    orig_n = n
    m = max(1, n // 3)
    k = n // 4
    l = n // 5

    d = (l + k) // m
    if (l + k) % m:
        d += 1
    if m * d > orig_n or orig_n - k < l:
        # print(-1)
        pass

    else:
        # print(d)
        pass
if __name__ == "__main__":
    main(1000)