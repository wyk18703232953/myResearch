def main(n):
    # 生成确定性输入数据：长度为 n 的非降序整数序列
    # 保证包含一些相邻差值为 1 或 0 的模式
    a = [(i // 2) for i in range(n)]

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
    main(10)