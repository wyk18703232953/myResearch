import sys
import random

def main(n):
    # 生成测试数据：sizes 为 1..n 的随机排列，cost 为 1..1000 的随机值
    sizes = list(range(1, n + 1))
    random.shuffle(sizes)
    cost = [random.randint(1, 1000) for _ in range(n)]

    tot = []
    for i in range(n):
        tot.append([sizes[i], cost[i]])

    ret = False
    lcomp = []
    for j in range(len(tot)):
        if j > 0 and j < len(tot) - 1:
            temp1 = tot[:j]
            temp2 = tot[j + 1:]
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
    # 示例：规模为 5
    main(5)