def main(n):
    # n 表示序列长度
    if n <= 0:
        # print(0)
        pass
        return

    # 构造确定性输入序列 m：这里使用 m[i] = i % 5 的模式
    m = [str(i % 5) for i in range(n)]

    j = 0
    mark = [1]
    for i in range(1, len(m)):
        tmp = max(mark[i - 1], int(m[i]) + 1)
        mark.append(tmp)

    j += mark[len(m) - 1] - int(m[len(m) - 1]) - 1
    for i in range(len(m) - 2, -1, -1):
        if mark[i] < mark[i + 1] - 1:
            mark[i] = mark[i + 1] - 1
        j += mark[i] - int(m[i]) - 1
    # print(j)
    pass
if __name__ == "__main__":
    main(10)