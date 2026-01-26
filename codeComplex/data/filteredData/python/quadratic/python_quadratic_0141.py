import math

mod = 10 ** 9 + 7

def get_original_pieces(x):
    common = (pow(x, 2) - 1) // 2
    first_piece = "10" * common + "1"
    second_piece = "0" + "10" * common
    return [first_piece, second_piece]

def main(n):
    # n is the board size (same meaning as original problem)
    size = n * n

    # generate four deterministic chessboard-like pieces of size n x n
    # piece 0: standard chessboard starting with '0'
    # piece 1: standard chessboard starting with '1'
    # piece 2: row-wise pattern: row parity (0/1)
    # piece 3: column-wise pattern: column parity (0/1)
    pieces_rows = [[] for _ in range(4)]
    for i in range(n):
        row0 = []
        row1 = []
        row2 = []
        row3 = []
        for j in range(n):
            row0.append(str((i + j) % 2))
            row1.append(str((i + j + 1) % 2))
            row2.append(str(i % 2))
            row3.append(str(j % 2))
        pieces_rows[0].append("".join(row0))
        pieces_rows[1].append("".join(row1))
        pieces_rows[2].append("".join(row2))
        pieces_rows[3].append("".join(row3))

    pieces = ["".join(pieces_rows[i]) for i in range(4)]

    original_pieces = get_original_pieces(n)
    till = size
    fp = [[0, i] for i in range(4)]
    sp = [[0, i] for i in range(4)]

    for i in range(4):
        fpc = 0
        spc = 0
        for j in range(till):
            if pieces[i][j] != original_pieces[0][j]:
                fpc += 1
            if pieces[i][j] != original_pieces[1][j]:
                spc += 1
        fp[i][0] = fpc
        sp[i][0] = spc

    fp.sort()
    sp.sort()

    ans1 = fp[0][0] + fp[1][0]
    ans2 = sp[0][0] + sp[1][0]

    for i in range(4):
        if sp[i][1] not in (fp[0][1], fp[1][1]):
            ans1 += sp[i][0]
        if fp[i][1] not in (sp[0][1], sp[1][1]):
            ans2 += fp[i][0]

    ans = min(ans1, ans2)
    # print(ans)
    pass
    return ans

if __name__ == "__main__":
    main(3)