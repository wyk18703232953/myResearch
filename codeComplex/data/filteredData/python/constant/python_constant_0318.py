import random

def main(n):
    # 生成测试数据：长度固定为14的非负整数列表
    # n 作为规模参数，这里用于控制生成数值的大小
    # 例如每个元素在 [0, 10*n] 之间
    max_val = max(1, 10 * n)
    l = [random.randint(0, max_val) for _ in range(14)]

    m = -1
    idx = 0
    while idx < 14:
        c = 0
        g = l.copy()
        div = l[idx] // 14
        h = l[idx] % 14
        i = idx + 1
        total = div * 14
        g[idx] = 0

        # 均匀分配 div
        while total:
            if i == 14:
                i = 0
            g[i] += div
            total -= div
            i += 1

        # 再分配剩余 h 个
        i = idx + 1
        while h:
            if i == 14:
                i = 0
            g[i] += 1
            h -= 1
            i += 1

        # 统计偶数之和
        for val in g:
            if val % 2 == 0:
                c += val

        m = max(m, c)
        idx += 1

    print(m)


if __name__ == "__main__":
    # 示例：调用 main，规模参数可自行调整
    main(10)