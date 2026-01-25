def main(n):
    # n 表示数组长度
    if n <= 0:
        return

    # 确定性构造：前 n-1 个为偶数，最后一个为奇数
    # 这样程序会找到唯一的奇数，并输出其位置 n
    a = [(i + 1) * 2 for i in range(n - 1)] + [2 * n + 1]

    chet = 0
    ne_chet = 0
    chet1 = []
    ne_chet1 = []
    for i in range(len(a)):
        if a[i] % 2 == 0:
            chet += 1
            chet1.append(a[i])
        else:
            ne_chet += 1
            ne_chet1.append(a[i])
        if chet >= 1 and ne_chet >= 1 and (chet > 1 or ne_chet > 1):
            break
    if chet == 1:
        print(a.index(chet1[0]) + 1)
    elif ne_chet == 1:
        print(a.index(ne_chet1[0]) + 1)


if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n
    main(10)