def get_original_pieces(x):
    common = (pow(x, 2) - 1) // 2
    first_piece = "10" * common + "1"
    second_piece = "0" + "10" * common
    return [first_piece, second_piece]


def generate_pieces(n):
    # Deterministically generate 4 chessboard-like pieces of size n*n
    # Using a simple pattern depending on (i + j) parity and piece index
    pieces = []
    for p in range(4):
        chars = []
        for i in range(n):
            for j in range(n):
                # Different patterns for each piece index
                if p == 0:
                    c = (i + j) % 2
                elif p == 1:
                    c = (i * j) % 2
                elif p == 2:
                    c = (i % 2)

                else:
                    c = (j % 2)
                chars.append("1" if c == 0 else "0")
        pieces.append("".join(chars))
    return pieces


def solve_for_n(n):
    pieces = generate_pieces(n)
    original_pieces = get_original_pieces(n)
    till = pow(n, 2)
    fp = [[0, i] for i in range(4)]
    sp = [[0, i] for i in range(4)]
    for i in range(4):
        fpc, spc = 0, 0
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
    return ans


def main(n):
    # n is the board size of each piece (n x n)
    result = solve_for_n(n)
    # print(result)
    pass
if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    main(5)