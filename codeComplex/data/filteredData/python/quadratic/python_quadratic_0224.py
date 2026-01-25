def main(n):
    # n 表示元素数量
    if n <= 0:
        print(-1)
        return

    # 确定性构造 sizes 和 cost
    sizes = [(i * 3) % (n + 5) + 1 for i in range(n)]
    cost = [(i * 7) % (2 * n + 10) + 1 for i in range(n)]

    tot = []
    for i in range(n):
        tot.append([sizes[i], cost[i]])

    import sys
    ret = False
    lcomp = []
    for j in range(len(tot)):
        if j > 0 and j < len(tot) - 1:
            temp1 = tot[:j]
            temp2 = tot[j + 1 :]
            mi_1 = sys.maxsize
            ret1 = False
            for i in range(len(temp1)):
                if temp1[i][0] < tot[j][0]:
                    mi_1 = min(mi_1, temp1[i][1])
                    ret1 = True
            mi_2 = sys.maxsize
            ret2 = False
            for k in range(len(temp2)):
                if temp2[k][0] > tot[j][0]:
                    mi_2 = min(mi_2, temp2[k][1])
                    ret2 = True
            if ret1 and ret2:
                ret = True
                lcomp.append(mi_1 + tot[j][1] + mi_2)
    if ret:
        print(min(lcomp))
    else:
        print(-1)


if __name__ == "__main__":
    # 示例调用，使用一个固定规模
    main(10)