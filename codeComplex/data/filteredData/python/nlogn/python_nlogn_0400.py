def main(n):
    # Deterministic generation of input pairs (x, y) and indices
    v = []
    for i in range(n):
        x = (i + 1) * ((i % 7) + 1)
        y = (i + 2) * ((i % 5) + 1)
        v.append([x, y, i])

    # Deterministic "shuffle" replacement: sort by a fixed key
    # This keeps behavior deterministic and scalable
    v.sort(key=lambda item: (item[0] * 131 + item[1] * 97 + item[2]))

    x = 0
    y = 0
    ans = [0] * n
    for i in range(n):
        nx1 = x + v[i][0]
        ny1 = y + v[i][1]
        nx2 = x - v[i][0]
        ny2 = y - v[i][1]
        if nx1 * nx1 + ny1 * ny1 < nx2 * nx2 + ny2 * ny2:
            x = nx1
            y = ny1
            ans[v[i][2]] = 1
        else:
            x = nx2
            y = ny2
            ans[v[i][2]] = -1

    # Mimic original stopping condition once (no loop)
    if x * x + y * y <= 1500000 ** 2:
        print(*ans)
    else:
        print(*ans)


if __name__ == "__main__":
    main(10)