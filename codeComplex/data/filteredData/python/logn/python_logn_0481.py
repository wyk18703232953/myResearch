def main(n):
    # 根据规模 n 生成测试数据：这里令 k = n
    # 若需其他生成方式，可在此修改
    k = n

    def cnt_special(N):
        if N == 0:
            return 0
        return cnt_special(N - 1) + N * (pow(10, N) - pow(10, N - 1))

    def cnt_digit(N):
        ord_len = len(str(N))
        bound = ord_len - 1
        return cnt_special(bound) + ord_len * (N + 1 - 10 ** bound)

    if k < 10:
        print(k)
    else:
        l = 1
        r = int(1e12)
        while r - l > 1:
            med = (r + l) // 2
            if cnt_digit(med) >= k:
                r = med
            else:
                l = med
        # cnt_digit(l) < k <= cnt_digit(r)
        rep = k - cnt_digit(l)
        print(str(r)[rep - 1])


if __name__ == "__main__":
    # 示例：调用 main(15)
    main(15)