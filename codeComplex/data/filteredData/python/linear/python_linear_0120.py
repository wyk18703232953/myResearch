def main(n):
    # 构造父节点数组 p[2..n]，保证是一棵树
    # 这里使用简单的确定性规则：p[i] = i // 2
    g = {}
    for i in range(1, n):
        p = (i + 1) // 2
        if p in g:
            g[p].append(i + 1)
        else:
            g[p] = [i + 1]

    ams = 'YES'
    for i in g:
        c = 0
        for j in g[i]:
            if j not in g:
                c += 1
        if c < 3:
            ams = 'NO'
    print(ams)


if __name__ == "__main__":
    main(10)