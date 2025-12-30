import random

def main(n):
    # 生成一棵以 0 为根的随机树的父节点数组 p（长度 n-1）
    # p[i] 表示节点 i+1 的父节点编号（0 到 i 之间的一个数，保证是树）
    p = [random.randint(0, i) for i in range(n - 1)]

    tr = {}
    for i in range(n - 1):
        if not tr.get(p[i]):
            tr[p[i]] = []
        tr[p[i]].append(i + 1)

    lc = [-1 for _ in range(n)]

    def get_lc(i):
        if lc[i] == -1:
            if tr.get(i):
                lc[i] = 0
                for j in tr[i]:
                    lc[i] += get_lc(j)
            else:
                lc[i] = 1
        return lc[i]

    for i in range(n - 1, -1, -1):
        get_lc(i)

    print(*sorted(lc))


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)