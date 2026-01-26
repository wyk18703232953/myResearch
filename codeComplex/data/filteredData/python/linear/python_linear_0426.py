def main(n):
    # 构造一个确定性的二维列表，每行长度为 (i % 5) + 1
    a = []
    t = None
    for i in range(n):
        # 第 i 行的数据：[(i + 1) * (j + 1) for j in range((i % 5) + 1)]
        row_len = (i % 5) + 1
        l = [(i + 1) * (j + 1) for j in range(row_len)]
        if i == 0:
            t = sum(l)
        a.append(sum(l))
    a.sort(reverse=True)
    # t 在构造中必定存在
    # print(a.index(t) + 1)
    pass
if __name__ == "__main__":
    main(10)