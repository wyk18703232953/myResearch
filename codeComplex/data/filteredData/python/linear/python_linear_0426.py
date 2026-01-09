def main(n):
    a = []
    t = None
    for i in range(n):
        # 确定性生成每一行的数据，行长度为 i+1
        l = [(i + 1) * (j + 1) for j in range(i + 1)]
        if i == 0:
            t = sum(l)
        a.append(sum(l))
    a.sort(reverse=True)
    # print(a.index(t) + 1)
    pass
if __name__ == "__main__":
    main(10)