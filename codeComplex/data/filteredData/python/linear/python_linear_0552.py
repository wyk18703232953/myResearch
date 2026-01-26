def main(n):
    # n 表示数组长度
    a = [i // 2 for i in range(n)]  # 确定性构造一个非严格递增整数序列

    max_el = -1
    er = -1
    for i in range(len(a)):
        if a[i] - max_el > 1:
            er = i + 1
            break
        if a[i] > max_el:
            max_el = a[i]

    # print(er)
    pass
if __name__ == "__main__":
    # 示例：以 n = 10 作为规模运行
    main(10)