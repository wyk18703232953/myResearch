def main(n):
    if n < 1:
        return
    # 构造一个确定性的父节点数组 p，长度为 n+1，p[0]=p[1]=0
    # 对于 i>=2，令 p[i] = i//2，形成一棵以 1 为根的完全二叉树结构
    p = [0, 0] + [i // 2 for i in range(2, n + 1)]

    d = [0] * (n + 1)
    for i in range(n, 1, -1):
        if d[i] == 0:
            d[i] = 1
        d[p[i]] += d[i]
    if n == 1:
        d[1] = 1
    d = d[1:]
    d.sort()
    # print(*d)
    pass
if __name__ == "__main__":
    main(10)