def main(n):
    # Generate deterministic test data based on n
    # sizes and cost are both lists of length n
    sizes = [(i * 3) % (n + 7) + 1 for i in range(n)]
    cost = [(i * 5 + 2) % (n + 11) + 1 for i in range(n)]

    tot = []
    for i in range(n):
        tot.append([sizes[i], cost[i]])
    ret = False
    lcomp = []
    for j in range(len(tot)):
        if j > 0 and j < len(tot) - 1:
            temp1 = tot[:j]
            temp2 = tot[j + 1:]
            mi_1 = 2**63 - 1  # substitute for sys.maxsize
            ret1 = False
            for i in range(len(temp1)):
                if temp1[i][0] < tot[j][0]:
                    mi_1 = mi_1 if mi_1 < temp1[i][1] else temp1[i][1]
                    ret1 = True
            mi_2 = 2**63 - 1
            ret2 = False
            for k in range(len(temp2)):
                if temp2[k][0] > tot[j][0]:
                    mi_2 = mi_2 if mi_2 < temp2[k][1] else temp2[k][1]
                    ret2 = True
            if ret1 and ret2:
                ret = True
                lcomp.append(mi_1 + tot[j][1] + mi_2)
    if ret:
        # print(min(lcomp))
        pass

    else:
        # print(-1)
        pass
if __name__ == "__main__":
    main(1000)