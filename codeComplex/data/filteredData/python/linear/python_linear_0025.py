def main(n):
    # n 表示列表长度
    if n <= 0:
        return

    # 构造确定性整数列表 li，元素为 i 的简单函数
    li = [(i * 3 + 1) for i in range(1, n + 1)]

    lis = [x % 2 for x in li]

    if lis.count(0) > lis.count(1):
        # print(lis.index(1) + 1)
        pass

    else:
        # print(lis.index(0) + 1)
        pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 以进行规模化实验
    main(10)