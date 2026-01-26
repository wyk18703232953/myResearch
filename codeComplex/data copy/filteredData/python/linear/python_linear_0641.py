def main(n):
    # Deterministic data generation:
    # For given n, create an array a of length n with a mix of 1s and >1 integers.
    # Example scheme:
    # - a[i] = 1 when i is even
    # - a[i] = 2 + (i % 3) when i is odd
    if n <= 0:
        return
    a = [1 if i % 2 == 0 else 2 + (i % 3) for i in range(n)]

    os = 0
    oss = []
    nos = 0
    nos_0 = -1
    nos_1 = -1
    sumnos = 0
    for i in range(n):
        if a[i] == 1:
            os += 1
            oss.append(i + 1)

        else:
            sumnos += a[i]
            nos += 1
            if nos_0 == -1:
                nos_0 = i + 1
            nos_1 = i + 1

    if os <= sumnos - (2 * (nos - 1)):
        es = []
        oss_i = 0
        ans = nos - 1
        if os >= 1:
            ans += 1
            es.append((nos_0, oss[0]))
            oss_i += 1
        if os >= 2:
            ans += 1
            es.append((nos_1, oss[1]))
            oss_i += 1
        # print("YES", ans)
        pass
        prev_nos = -1
        for i in range(n):
            if a[i] > 1:
                if prev_nos != -1:
                    es.append((prev_nos + 1, i + 1))
                for _ in range(a[i] - 2):
                    if oss_i >= os:
                        break
                    es.append((i + 1, oss[oss_i]))
                    oss_i += 1
                prev_nos = i
        # print(len(es))
        pass
        for e in es:
            # print(*e)
            pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(10)