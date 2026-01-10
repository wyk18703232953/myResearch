def res(d, N):
    for i in range(1, N):
        if d[i][1] <= d[i - 1][1]:
            return str(d[i][2] + 1) + ' ' + str(d[i - 1][2] + 1)
    return '-1 -1'


def main(n):
    N = n
    d = []
    for i in range(N):
        a = i
        b = N - i
        d.append((a, b, i))
    d = sorted(d, key=lambda x: (x[0], -x[1]))
    result = res(d, N)
    print(result)


if __name__ == "__main__":
    main(10)