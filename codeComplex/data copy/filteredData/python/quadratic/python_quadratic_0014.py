def main(n):
    # Interpret n as the number of circle centers
    # Deterministic generation of xs: arithmetic progression with step 2
    r = 1
    xs = [2 * i for i in range(n)]
    ys = []
    for i in range(n):
        xi = xs[i]
        two_r = 2 * r
        two_r_sq = two_r * two_r
        best = None
        for j in range(i):
            diff = abs(xi - xs[j])
            if diff <= two_r:
                val = (two_r_sq - diff * diff) ** 0.5 + ys[j]
                if best is None or val > best:
                    best = val
        ys.append(best if best is not None else r)
    # print(*ys)
    pass
if __name__ == "__main__":
    main(10)