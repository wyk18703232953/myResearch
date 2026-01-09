def main(n):
    # 映射：n 为 ps 的长度，k 取一个与 256 相关的固定值，保证可规模化且确定
    # 例如：k = max(1, min(50, n // 4 + 1))
    k = max(1, min(50, n // 4 + 1))

    # 生成确定性的 ps 列表，元素范围限制在 [0, 255]
    # 使用简单算术构造：ps[i] = (i * 17 + 23) % 256
    ps = [(i * 17 + 23) % 256 for i in range(n)]

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

    # print("n =", n, "k =", k)
    pass
    # print("ps:", " ".join(str(x) for x in ps))
    pass
    # print("ans:", " ".join(str(x) for x in ans))
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要调整 n
    main(100)