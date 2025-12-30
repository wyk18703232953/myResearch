import random

def main(n):
    # 生成一组满足条件的 s（0 ~ n-1 的排列），并据此生成 l、r
    s = list(range(n))
    random.shuffle(s)

    l = [0] * n
    r = [0] * n

    # 计算每个位置的 l[i] 和 r[i]
    for i in range(n):
        ll = 0
        for j in range(i):
            if s[j] > s[i]:
                ll += 1
        rr = 0
        for j in range(i + 1, n):
            if s[j] > s[i]:
                rr += 1
        l[i] = ll
        r[i] = rr

    # 下方是原逻辑，只不过使用生成的 l 和 r
    fl = 0
    m = n
    s_rebuild = list(range(n))
    for i in range(n):
        s_rebuild[i] = m - (l[i] + r[i])
        if fl != 1 and s_rebuild[i] == m:
            fl = 1
    for i in range(n):
        ll = 0
        for j in range(i):
            if s_rebuild[j] > s_rebuild[i]:
                ll += 1
        rr = 0
        for j in range(i + 1, n):
            if s_rebuild[j] > s_rebuild[i]:
                rr += 1
        if l[i] != ll or rr != r[i]:
            fl = 0
            break

    if fl == 1 and l[0] == 0 and r[n - 1] == 0:
        print('YES')
        print(*s_rebuild)
    else:
        print('NO')


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)