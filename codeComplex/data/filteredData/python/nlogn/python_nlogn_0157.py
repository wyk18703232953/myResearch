import random

def main(n):
    # 生成测试数据
    # 为了简化，这里令 w, h 为与 n 同级的规模
    # 可以根据需要调整生成规则
    w = max(2, n + 1)
    h = max(2, n + 1)

    # 初始化切割数组
    l, r = [-1] * (w + 1), [-1] * (w + 1)
    t, b = [-1] * (h + 1), [-1] * (h + 1)
    l[0], b[0], t[h], r[w] = 0, 0, h, w
    V, H = [0] * n, [0] * n

    # 随机生成切割位置与方向
    # 为确保合法性：竖切位置在 [1, w-1]，横切位置在 [1, h-1]
    for i in range(n):
        if random.random() < 0.5:
            line = 'V'
            idx = random.randint(1, w - 1)
            r[idx] = w
            V[i] = idx
        else:
            line = 'H'
            idx = random.randint(1, h - 1)
            t[idx] = h
            H[i] = idx

    # 预处理竖向分段及最大宽度
    left, max_w = 0, 0
    for i in range(1, w + 1):
        if r[i] != -1:
            l[i] = left
            r[left] = i
            max_w = max(max_w, i - left)
            left = i

    # 预处理横向分段及最大高度
    bottom, max_h = 0, 0
    for i in range(1, h + 1):
        if t[i] != -1:
            b[i] = bottom
            t[bottom] = i
            max_h = max(max_h, i - bottom)
            bottom = i

    # 逆向恢复时每一步的最大矩形面积
    res = [0] * n
    res[n - 1] = max_h * max_w
    for i in range(n - 1, 0, -1):
        if V[i] != 0:
            # 撤销一次竖切
            max_w = max(max_w, r[V[i]] - l[V[i]])
            r[l[V[i]]] = r[V[i]]
            l[r[V[i]]] = l[V[i]]
        else:
            # 撤销一次横切
            max_h = max(max_h, t[H[i]] - b[H[i]])
            b[t[H[i]]] = b[H[i]]
            t[b[H[i]]] = t[H[i]]
        res[i - 1] = max_h * max_w

    # 输出结果
    for x in res:
        print(x)


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)