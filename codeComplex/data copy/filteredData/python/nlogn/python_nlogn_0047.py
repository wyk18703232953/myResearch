def main(n):
    # n 表示列表长度
    if n <= 0:
        return
    # 确定性生成长度为 n 的整数列表
    l = [(i % 5) + 1 for i in range(n)]
    l = sorted(l)
    if l[-1] == 1:
        l[-1] = 2

    else:
        l[-1] = 1
    l = sorted(l)
    # print(*l)
    pass
if __name__ == "__main__":
    main(10)