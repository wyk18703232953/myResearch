def main(n):
    # 生成一个长度为 n 的整数数组，其中：
    # 前 n-1 个元素为奇数，最后一个为偶数
    # 这样偶数位置唯一且确定，算法将输出 n
    arr = [(2 * i + 1) for i in range(n - 1)] + [2 * n]

    codd = 0
    ceven = 0
    ptodd = -1
    pteven = -1

    for i in range(n):
        if arr[i] % 2 == 0:
            ceven += 1
            pteven = i
        else:
            codd += 1
            ptodd = i

    if ceven == 1:
        print(pteven + 1)
    else:
        print(ptodd + 1)


if __name__ == "__main__":
    main(10)