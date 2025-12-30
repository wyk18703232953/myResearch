import random

def main(n: int):
    # 根据规模 n 生成测试数据
    # 这里假设 w, h 的量级与 n 同阶，可根据需要调整生成策略
    if n <= 0:
        return

    # 生成宽和高（至少要比切割次数略大，否则没有意义）
    w = max(2, n + 1)
    h = max(2, n + 1)

    # 生成 n 次切割操作
    # 每次切割含义与原程序一致：("V" or "H", index)
    # index 范围：1..w-1（垂直切割），1..h-1（水平切割）
    ops = []
    for _ in range(n):
        if random.choice([True, False]):  # 垂直切割
            line = "V"
            index = random.randint(1, w - 1)
        else:  # 水平切割
            line = "H"
            index = random.randint(1, h - 1)
        ops.append((line, index))

    # -------- 原逻辑开始（移除 input()，使用 w,h,n,ops） --------

    l = [-1] * (w + 1)
    r = [-1] * (w + 1)
    t = [-1] * (h + 1)
    b = [-1] * (h + 1)

    l[0] = 0
    b[0] = 0
    t[h] = h
    r[w] = w

    V = [0] * n
    H = [0] * n
    for i in range(n):
        line, index = ops[i]
        if line == "V":
            r[index] = w
            V[i] = index
        else:
            t[index] = h
            H[i] = index

    left = 0
    mxw = 0
    for i in range(1, w + 1):
        if r[i] != -1:
            l[i] = left
            r[left] = i
            mxw = max(mxw, i - left)
            left = i

    bottom = 0
    mxh = 0
    for i in range(1, h + 1):
        if t[i] != -1:
            b[i] = bottom
            t[bottom] = i
            mxh = max(mxh, i - bottom)
            bottom = i

    ans = [0] * n
    ans[n - 1] = mxh * mxw

    for i in range(n - 1, 0, -1):
        if V[i] != 0:
            mxw = max(mxw, r[V[i]] - l[V[i]])
            r[l[V[i]]] = r[V[i]]
            l[r[V[i]]] = l[V[i]]
        else:
            mxh = max(mxh, t[H[i]] - b[H[i]])
            b[t[H[i]]] = b[H[i]]
            t[b[H[i]]] = t[H[i]]
        ans[i - 1] = mxh * mxw

    for v in ans:
        print(v)


# 示例：调用 main(5)
if __name__ == "__main__":
    main(5)