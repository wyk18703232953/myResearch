def main(n):
    # 将 n 映射为两个列表的长度
    # 为了有交集，l1 用偶数，l2 用从某处开始的一段偶数
    size1 = max(1, n)
    size2 = max(1, n)

    # 确定性构造：l1 = [2*i for i in range(size1)]
    # l2 = [2*i for i in range(size2 // 2, size2 // 2 + size2)]
    l1 = [2 * i for i in range(size1)]
    start2 = size2 // 2
    l2 = [2 * (start2 + i) for i in range(size2)]

    for i in l1:
        if i in l2:
            # print(i, end=" ")
            pass
if __name__ == "__main__":
    # 示例调用，实际实验时可自行修改 n
    main(10)