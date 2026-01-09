def main(n):
    arr1 = tuple(i % (n // 2 + 1) for i in range(n))
    arr2 = tuple((n - 1 - i) % (n // 2 + 1) for i in range(n))

    d = dict()
    ans = [0] * n

    for i in range(n):
        d[i] = [arr1[i], arr2[i]]

    def run():
        for nn in range(n, 0, -1):
            s = list()
            for i in d:
                if d[i][0] == d[i][1] == 0:
                    s.append(i)
                    ans[i] = nn

            if s:
                for i in s:
                    del d[i]
                for i in d:
                    l = r = 0
                    for j in s:
                        if j < i:
                            l += 1

                        else:
                            r += 1
                    if d[i][0] >= l:
                        d[i][0] -= l

                    else:
                        return
                    if d[i][1] >= r:
                        d[i][1] -= r

                    else:
                        return

            else:
                return

    run()

    if 0 in ans:
        # print('NO')
        pass

    else:
        # print('YES')
        pass
        # print(*ans, sep=' ')
        pass
if __name__ == "__main__":
    main(10)