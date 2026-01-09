def main(n):
    # Interpret n as the length of the sequence ps.
    # Deterministic construction of (n, k, ps):
    # Keep k in a reasonable range relative to value space [0,255].
    # Use values in [0, 255] to be consistent with original g,f arrays.
    if n <= 0:
        return

    # Choose k deterministically as a function of n, at least 1.
    k = (n % 10) + 1

    # Deterministic generation of ps: cycle through 0..255 using a simple arithmetic pattern.
    ps = [(i * 37 + 11) % 256 for i in range(n)]

    if k == 1:
        # print(' '.join(str(i) for i in ps))
        pass
        return

    g = [None for _ in range(256)]
    f = [None for _ in range(256)]
    ans = []
    for i in range(n):
        p = ps[i]
        if g[p] is not None:
            ans.append(g[p])
            f[p] = 1

        else:
            gb = 0
            for j in range(1, k):
                ind = p - j
                if ind < 0 or ind >= 256:
                    break
                if f[ind] is not None:
                    gb = ind + 1
                    break
                if ind <= 0:
                    break
                if j == k - 1:
                    gb = ind
            ans.append(gb)
            for j in range(k):
                if gb + j >= 256:
                    break
                if f[gb + j] is None:
                    g[gb + j] = gb

                else:
                    break
            if 0 <= gb < 256:
                f[gb] = 1
            if 0 <= p < 256:
                f[p] = 1
    # print(' '.join(str(i) for i in ans))
    pass
if __name__ == "__main__":
    main(10)