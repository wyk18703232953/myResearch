def main(n):
    # 生成确定性的输入数据：n 个整数，值为 i % 5
    m = [str(i % 5) for i in range(n)]
    mark = [1]
    j = 0
    for i in range(1, len(m)):
        tmp = max(mark[i - 1], int(m[i]) + 1)
        mark.append(tmp)
    j += mark[len(m) - 1] - int(m[len(m) - 1]) - 1
    for i in range(len(m) - 2, -1, -1):
        if mark[i] < mark[i + 1] - 1:
            mark[i] = mark[i + 1] - 1
        j += mark[i] - int(m[i]) - 1
    print(j)


if __name__ == "__main__":
    main(10)