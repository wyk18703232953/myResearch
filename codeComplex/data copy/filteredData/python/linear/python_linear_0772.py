def main(n):
    # 对应原始输入结构：n, m, k = map(int, input().split())
    # 这里将 n 作为原来的 n，m = n，k = max(1, n // 3)
    n_val = max(1, n)
    m = n_val
    k = max(1, n_val // 3)

    # 构造确定性的 P 列表，对应原来的第二行输入
    # 保证 1 <= P[i] <= n_val，且有重复和分布变化，便于复杂度实验
    P = [((i * 2 + 3) % n_val) + 1 for i in range(m)]

    # 原程序逻辑
    P.reverse()
    ops = 0
    i = 1
    while P:
        nxt = P[-1]
        togo = nxt - i
        skip = togo // k * k
        i += skip

        space = k
        while space:
            special = 0
            while P and P[-1] < i + space:
                special += 1
                P.pop()
            i += space
            if not special:
                break
            ops += 1
            space = special

    # print(ops)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(10)