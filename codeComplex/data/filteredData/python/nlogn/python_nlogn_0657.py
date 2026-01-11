def main(n):
    # Deterministic generation of input:
    # n: number of vertices
    # a: degrees, deterministic pattern
    if n <= 0:
        return
    a = [(i % (n // 2 + 1)) + 1 for i in range(1, n + 1)]

    def out_edge(x, y, a_local, outres_local):
        a_local[x - 1] -= 1
        a_local[y - 1] -= 1
        outres_local.append((x, y))

    sa = sum(a)
    ma = min(a)
    if (sa < 2 * (n - 1)) or (ma < 1):
        # print('NO')
        pass
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
    # print('YES', min(n - 1, path_len))
    pass

    reserve_start = 0
    while kk < n:
        if verts[reserve_start][1] > 0:
            outres.append((verts[reserve_start][0], verts[kk][0]))
            verts[reserve_start][1] -= 1
            verts[kk][1] -= 1
            kk += 1

        else:
            reserve_start += 1

    # print(len(outres))
    pass
    for oo in outres:
        # print(*oo)
        pass
if __name__ == "__main__":
    main(10)