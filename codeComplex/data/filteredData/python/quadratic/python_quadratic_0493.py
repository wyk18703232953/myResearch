def main(n):
    # n: problem size, here used as the length of the two arrays
    if n <= 0:
        return

    # Deterministic generation of arr1 and arr2 based on n
    # Example: small bounded values to keep behavior meaningful
    arr1 = tuple((i % 3) for i in range(n))
    arr2 = tuple(((n - 1 - i) % 3) for i in range(n))

    d = {}
    ans = [0] * n

    for i in range(n):
        d[i] = [arr1[i], arr2[i]]

    def run():
        for nn in range(n, 0, -1):
            s = []
            for i in d:
                if d[i][0] == d[i][1] == 0:
                    s.append(i)
                    ans[i] = nn

            if s:
                for i in s:
                    del d[i]
                for i in d:
                    l = 0
                    r = 0
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
    # Example deterministic call; adjust n as needed for experiments
    main(10)