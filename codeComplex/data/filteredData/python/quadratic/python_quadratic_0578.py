def main(n):
    # Interpret n as: number of test cases = n,
    # each with string length = n and k = max(1, n // 2)
    q = n
    if q <= 0:
        return

    # Deterministically generate test cases
    tests = []
    for t in range(q):
        length = n
        k = n // 2 if n // 2 > 0 else 1
        # Generate a deterministic RGB string of length 'length'
        chars = ['R', 'G', 'B']
        l = ''.join(chars[(i + t) % 3] for i in range(length))
        tests.append((length, k, l))

    b = []
    for idx in range(q):
        n_case, k, l = tests[idx]
        k1 = 'R'
        k2 = 'G'
        k3 = 'B'
        for i in range(1, k):
            if k1[i - 1] == 'R':
                k1 = k1 + 'G'
            if k1[i - 1] == 'G':
                k1 = k1 + 'B'
            if k1[i - 1] == 'B':
                k1 = k1 + 'R'
            if k2[i - 1] == 'R':
                k2 = k2 + 'G'
            if k2[i - 1] == 'G':
                k2 = k2 + 'B'
            if k2[i - 1] == 'B':
                k2 = k2 + 'R'
            if k3[i - 1] == 'R':
                k3 = k3 + 'G'
            if k3[i - 1] == 'G':
                k3 = k3 + 'B'
            if k3[i - 1] == 'B':
                k3 = k3 + 'R'
        minn = n_case
        if n_case - k + 1 > 0:
            for i in range(n_case - k + 1):
                tec = 0
                for j in range(k):
                    if l[i + j] != k1[j]:
                        tec += 1
                if tec < minn:
                    minn = tec
            for i in range(n_case - k + 1):
                tec = 0
                for j in range(k):
                    if l[i + j] != k2[j]:
                        tec += 1
                if tec < minn:
                    minn = tec
            for i in range(n_case - k + 1):
                tec = 0
                for j in range(k):
                    if l[i + j] != k3[j]:
                        tec += 1
                if tec < minn:
                    minn = tec
        b.append(minn)

    for i in range(q):
        # print(b[i])
        pass
if __name__ == "__main__":
    main(5)