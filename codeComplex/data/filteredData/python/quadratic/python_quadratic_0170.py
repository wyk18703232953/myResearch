import random

def main(n):
    # 这里根据 n 自动生成测试数据：
    # 1) 随机生成 k，范围 [1, 20] 且不超过 255
    # 2) 随机生成 n 个 p，范围 [0, 255]
    k = random.randint(1, min(20, 255))
    ps = [random.randint(0, 255) for _ in range(n)]

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
                    gb = ind
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
    # 示例：调用 main(10)
    main(10)