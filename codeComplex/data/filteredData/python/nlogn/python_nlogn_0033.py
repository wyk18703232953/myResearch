def main(n):
    # n 表示输入列表的长度
    # 生成确定性整数列表，包含重复元素：如 [0, 1, 2, ..., n-1, 0, 1, 2, ..., n-1]
    l1 = [i % max(1, n // 2 + 1) for i in range(n)]

    l2 = []
    for i in l1:
        l2.append(int(i))
    l1 = set(l2)
    l1 = list(l1)
    for i in range(0, len(l1)):
        for j in range(i + 1, len(l1)):
            if l1[i] > l1[j]:
                temp = l1[j]
                l1[j] = l1[i]
                l1[i] = temp
    if len(l1) > 1:
        # print(l1[1])
        pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    main(10)