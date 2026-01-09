def fis(sq):
    if sq[2] < sq[0] or sq[3] < sq[1]:
        return [0, 0]
    sc = (sq[0] + sq[1]) % 2
    fc = (sq[2] + sq[3]) % 2
    sxl = sq[2] - sq[0] + 1
    syl = sq[3] - sq[1] + 1
    hf = (sxl * syl) // 2
    cp = -1
    if sc == fc and (sxl + syl) % 2 == 0 and sxl % 2 == 1:
        cp = sc
    return [hf + (1 if cp == 0 else 0), hf + (1 if cp == 1 else 0)]


def main(n):
    t = n
    results = []
    for i in range(t):
        # Deterministic generation of n, m for each test
        rows = i + 2
        cols = i + 3
        # Deterministic white rectangle [x1, y1, x2, y2]
        wco = [1, 1, min(2 + i, cols), min(2 + i, rows)]
        # Deterministic black rectangle [x1, y1, x2, y2]
        bco = [max(1, cols - i), max(1, rows - i), cols, rows]

        wf, bf = fis([1, 1, cols, rows])
        btw = fis(wco)[1]
        wtb = fis(bco)[0]
        bnac = [
            max(wco[0], bco[0]),
            max(wco[1], bco[1]),
            min(wco[2], bco[2]),
            min(wco[3], bco[3]),
        ]
        bna = fis(bnac)[1]
        results.append((wf + btw - wtb - bna, bf + wtb - btw + bna))

    for res in results:
        # print(res[0], res[1])
        pass
if __name__ == "__main__":
    main(5)