def main(n):
    # Deterministic generation of input array a of length n
    # Ensure both 1s and values >1 exist for meaningful behavior
    if n <= 0:
        return

    a = []
    for i in range(n):
        # Construct values deterministically:
        # mix of 1 and values >1 based on index
        if i % 3 == 0:
            a.append(1)

        else:
            # values from 2 to 5 deterministically
            a.append(2 + (i % 4))

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
    # Example call for time complexity experiments
    main(10)