def main(n):
    # 生成确定性输入数据
    # n 至少为 2，保证有意义的 n 和 k
    if n < 2:
        n = 2
    # 设定 k 的规模：在 [1, min(10, n)] 范围内确定性映射
    k = (n % 10) + 1
    if k > n:
        k = n
    # 生成 ps：长度为 n，元素在 [0, 255] 内循环
    ps = [i % 256 for i in range(n)]

    # 原算法逻辑
    if k == 1:
        print(' '.join(str(i) for i in ps))
        return

    g = [None for _ in range(256)]
    f = [None for _ in range(256)]
    ans = []
    for i in range(n):
        p = ps[i]
        if g[p] is not None:
            ans.append(g[p])
            f[p] = 1
        else:
            gb = 0
            for j in range(1, k):
                ind = p - j
                if ind < 0:
                    break
                if f[ind] is not None:
                    gb = ind + 1
                    break
                if ind <= 0:
                    break
                if j == k - 1:
                    gb = ind
            ans.append(gb)
            for j in range(k):
                if gb + j >= 256:
                    break
                if f[gb + j] is None:
                    g[gb + j] = gb
                else:
                    break
            f[gb] = 1
            f[p] = 1
    print(' '.join(str(i) for i in ans))


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(10)