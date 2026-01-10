def main(n):
    # n 表示数组长度
    if n <= 0:
        return

    # 确定性生成长度为 n 的数组 a
    # 生成方式：a[i] = i * (-1) ** i
    a = [i if i % 2 == 0 else -i for i in range(n)]

    for i, x in enumerate(a):
        if x >= 0:
            a[i] = -x - 1

    cnt_neg = 0
    for x in a:
        if x < 0:
            cnt_neg += 1

    b = sorted((abs(x), i) for i, x in enumerate(a))
    if cnt_neg % 2 == 1:
        ind = b[n - 1][1]
        a[ind] = -a[ind] - 1

    print(' '.join(map(str, a)))


if __name__ == "__main__":
    main(10)