import random

def main(n):
    # 生成满足条件的测试数据 a
    # 条件：每个 a[i] >= 1 且 sum(a) >= 2*(n-1)
    if n <= 0:
        return

    # 先生成每个点至少 1 度
    a = [1] * n
    base_sum = sum(a)
    need = 2 * (n - 1) - base_sum
    if need < 0:
        need = 0

    # 随机把多余的度数分配给点
    # 额外再加上一些随机度数，保证有多样性
    extra = need + random.randint(0, max(0, 2 * n))
    for _ in range(extra):
        idx = random.randint(0, n - 1)
        a[idx] += 1

    # 原算法逻辑开始
    sa = sum(a)
    ma = min(a)
    if (sa < 2 * (n - 1)) or (ma < 1):
        print('NO')
        return

    verts = sorted(enumerate(a, 1), key=lambda x: x[1], reverse=True)
    verts = [list(j) for j in verts]
    outres = []

    kk = 1
    for kk in range(1, n):
        if verts[kk - 1][1] >= 1:
            outres.append((verts[kk][0], verts[kk - 1][0]))
            verts[kk][1] -= 1
            verts[kk - 1][1] -= 1
        else:
            break
    else:
        kk += 1

    path_len = kk
    print('YES', min(n - 1, path_len))

    reserve_start = 0
    while kk < n:
        if verts[reserve_start][1] > 0:
            outres.append((verts[reserve_start][0], verts[kk][0]))
            verts[reserve_start][1] -= 1
            verts[kk][1] -= 1
            kk += 1
        else:
            reserve_start += 1

    print(len(outres))
    for oo in outres:
        print(*oo)


if __name__ == "__main__":
    # 示例：运行规模为 n 的测试
    main(5)