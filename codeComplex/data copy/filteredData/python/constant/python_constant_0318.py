def main(n):
    # 生成一个长度为 14 的确定性整数列表，规模由 n 控制
    l = [(i * n + i * i) % 100 for i in range(14)]

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

        # 均分 div*14
        while total:
            if i == 14:
                i = 0
            g[i] += div
            total -= div
            i += 1

        # 分配余数 h
        i = idx + 1
        while h:
            if i == 14:
                i = 0
            g[i] += 1
            h -= 1
            i += 1

        # 统计偶数和
        for val in g:
            if val % 2 == 0:
                c += val

        if c > m:
            m = c
        idx += 1

    return m


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    result = main(10)
    # print(result)
    pass