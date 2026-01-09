def main(n):
    # 确定性数据生成：n 行，每行长度为 3，元素为 i, i+1, i+2
    l = []
    for i in range(n):
        c = [i, i + 1, i + 2]
        l.append(sum(c))

    m = l[0]
    l.sort(reverse=True)
    for i in range(len(l)):
        if m == l[i]:
            # print(i + 1)
            pass
            break


if __name__ == "__main__":
    main(10)