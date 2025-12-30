import random

def main(n):
    # 这里根据 n 生成测试数据：n 和 ps
    # k 的取值可按需要调整策略，这里设为 1~min(n, 200) 之间的随机值
    if n <= 0:
        return

    # 生成 ps：每个元素在 1~255 之间
    ps = [random.randint(1, 255) for _ in range(n)]
    k = random.randint(1, min(n, 200))

    g = [None for _ in range(256)]
    f = [None for _ in range(256)]
    ans = []

    if k == 1:
        print(' '.join(str(i) for i in ps))
        return

    for i in range(n):
        p = ps[i]
        if g[p] is not None:
            ans.append(g[p])
            f[p] = 1
        else:
            gb = 0
            for j in range(1, k):
                ind = p - j
                if ind >= 0 and f[ind] is not None:
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