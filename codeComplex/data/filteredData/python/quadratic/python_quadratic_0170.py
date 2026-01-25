def main(n):
    # 将原来的输入结构映射为：
    # 第一行: n, k
    # 第二行: n 个整数 ps
    #
    # 这里将 n 作为序列长度，同时构造一个确定性的 k 和 ps：
    # - k = max(1, n // 4)，控制窗口大小，随规模增长
    # - ps 为长度为 n 的整数列表，值在 [0, 255] 范围内，使用简单算术生成
    if n <= 0:
        return

    k = max(1, n // 4)
    ps = [(i * 37 + 13) % 256 for i in range(n)]

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
            for j in range(k):
                ind = p - j
                if ind < 0:
                    break
                if f[ind] is not None:
                    gb = ind + 1
                    break
                if ind == 0:
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

    print(" ".join(str(x) for x in ans))


if __name__ == "__main__":
    # 示例调用：可以根据需要改变 n 来做规模实验
    main(10)