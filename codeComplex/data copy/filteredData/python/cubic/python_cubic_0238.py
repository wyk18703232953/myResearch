def main(n):
    # n controls the size of R, G, B and the arrays; ensure they are at least 1
    R = max(1, n)
    G = max(1, n)
    B = max(1, n)

    # Deterministic generation of Ra, Ga, Ba; then reverse sorted as in original
    Ra = sorted([i * 2 + 1 for i in range(R)], reverse=True)
    Ga = sorted([i * 3 + 2 for i in range(G)], reverse=True)
    Ba = sorted([i * 5 + 3 for i in range(B)], reverse=True)

    final_ans = 0

    dparr = [[[-1 for _ in range(B + 1)] for _ in range(G + 1)] for _ in range(R + 1)]

    # Initialize base states (only if corresponding arrays have at least 1 element)
    if R >= 1 and G >= 1:
        dparr[1][1][0] = Ra[0] * Ga[0]
        final_ans = max(final_ans, dparr[1][1][0])
    if R >= 1 and B >= 1:
        dparr[1][0][1] = Ra[0] * Ba[0]
        final_ans = max(final_ans, dparr[1][0][1])
    if G >= 1 and B >= 1:
        dparr[0][1][1] = Ga[0] * Ba[0]
        final_ans = max(final_ans, dparr[0][1][1])

    def add_ns(t1):
        x, y, z = t1
        if x + 1 <= R:
            if y + 1 <= G:
                if dparr[x + 1][y + 1][z] == -1:
                    queue.append((x + 1, y + 1, z))
                    dparr[x + 1][y + 1][z] = 0
            if z + 1 <= B:
                if dparr[x + 1][y][z + 1] == -1:
                    queue.append((x + 1, y, z + 1))
                    dparr[x + 1][y][z + 1] = 0
        if y + 1 <= G and z + 1 <= B:
            if dparr[x][y + 1][z + 1] == -1:
                queue.append((x, y + 1, z + 1))
                dparr[x][y + 1][z + 1] = 0

    def store_ans(t1):
        nonlocal final_ans
        x, y, z = t1
        if x - 1 >= 0 and y - 1 >= 0 and z >= 0 and dparr[x - 1][y - 1][z] != -1:
            dparr[x][y][z] = max(dparr[x][y][z], dparr[x - 1][y - 1][z] + Ra[x - 1] * Ga[y - 1])
        if x - 1 >= 0 and y >= 0 and z - 1 >= 0 and dparr[x - 1][y][z - 1] != -1:
            dparr[x][y][z] = max(dparr[x][y][z], dparr[x - 1][y][z - 1] + Ra[x - 1] * Ba[z - 1])
        if x >= 0 and y - 1 >= 0 and z - 1 >= 0 and dparr[x][y - 1][z - 1] != -1:
            dparr[x][y][z] = max(dparr[x][y][z], dparr[x][y - 1][z - 1] + Ga[y - 1] * Ba[z - 1])
        final_ans = max(final_ans, dparr[x][y][z])

    queue = []
    if R >= 1 and G >= 1:
        queue.append((1, 1, 0))
    if R >= 1 and B >= 1:
        queue.append((1, 0, 1))
    if G >= 1 and B >= 1:
        queue.append((0, 1, 1))

    for t in queue:
        add_ns(t)

    ptr = len(queue)
    while ptr < len(queue):
        store_ans(queue[ptr])
        add_ns(queue[ptr])
        ptr += 1

    # print(final_ans)
    pass
if __name__ == "__main__":
    main(3)