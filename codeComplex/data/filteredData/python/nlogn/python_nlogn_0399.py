def main(n):
    # deterministic data generation: v[i] = [i+1, (i+1)//2, i]
    v = [[i + 1, (i + 1) // 2, i] for i in range(n)]

    # replace random.shuffle with deterministic permutation
    # simple deterministic "shuffle": sort by (y, x, index) reversed
    v.sort(key=lambda p: (p[1], p[0], p[2]), reverse=True)

    x = 0
    y = 0
    ans = [0] * n
    for i in range(n):
        if (x + v[i][0]) ** 2 + (y + v[i][1]) ** 2 < (x - v[i][0]) ** 2 + (y - v[i][1]) ** 2:
            x += v[i][0]
            y += v[i][1]
            ans[v[i][2]] = 1
        else:
            x -= v[i][0]
            y -= v[i][1]
            ans[v[i][2]] = -1

    # keep the same termination condition logic, but run only once
    if x * x + y * y <= 1500000 ** 2:
        print(*ans)
    else:
        print(*ans)


if __name__ == "__main__":
    main(10)