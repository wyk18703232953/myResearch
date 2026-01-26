def main(n):
    SIZE = 105
    a = [0] * SIZE
    b = [0] * SIZE

    # 确定性数据生成：构造 l, r
    # 让 l 和 r 都与 n 成比例增长，并保证 l <= r
    l = n * 2 + 1
    r = n * 3 + 5
    if l > r:
        l, r = r, l

    if l == r:
        result = 0

    else:
        len1 = 0
        len2 = 0
        temp_l = l
        temp_r = r

        while temp_l != 0 and len1 < SIZE:
            a[len1] = temp_l % 2
            temp_l = temp_l // 2
            len1 += 1

        while temp_r != 0 and len2 < SIZE:
            b[len2] = temp_r % 2
            temp_r = temp_r // 2
            len2 += 1

        tag = 0
        for i in range(max(len1, len2) - 1, 0, -1):
            if b[i] == 1 and a[i] == 0:
                tag = i
                break

        result = pow(2, tag + 1) - 1

    # print(result)
    pass
if __name__ == "__main__":
    main(10)