def main(n):
    # n 表示列表长度，生成确定性整数序列
    l = [(i * 2 + (i % 3)) for i in range(1, n + 1)]

    c1 = 0
    c2 = 0
    for i in l:
        if i % 2 == 0:
            c1 += 1
        else:
            c2 += 1

    lasteven = -1
    lastodd = -1
    for i in range(len(l) - 1, -1, -1):
        if l[i] % 2 == 0:
            lasteven = i
            break
    for i in range(len(l) - 1, -1, -1):
        if l[i] % 2 != 0:
            lastodd = i
            break

    if c1 == 1 and lasteven != -1:
        print(lasteven + 1)
    else:
        print(lastodd + 1 if lastodd != -1 else -1)


if __name__ == "__main__":
    main(10)