def main(n):
    # Interpret n as both:
    # - number of test cases q = n
    # - length parameter for each test: string length and k derived from it
    q = n
    b = []

    for m in range(q):
        # For each test, deterministically define n_local and k
        # n_local grows with m and overall n to scale workload
        n_local = max(1, n + m)
        # k is at most n_local and at least 1
        k = max(1, (m % n_local) + 1)

        # Deterministically generate string l of length n_local over 'R','G','B'
        colors = ['R', 'G', 'B']
        l = ''.join(colors[(i + m) % 3] for i in range(n_local))

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

        minn = n_local

        for i in range(n_local - k + 1):
            tec = 0
            for j in range(k):
                if l[i + j] != k1[j]:
                    tec += 1
            if tec < minn:
                minn = tec

        for i in range(n_local - k + 1):
            tec = 0
            for j in range(k):
                if l[i + j] != k2[j]:
                    tec += 1
            if tec < minn:
                minn = tec

        for i in range(n_local - k + 1):
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