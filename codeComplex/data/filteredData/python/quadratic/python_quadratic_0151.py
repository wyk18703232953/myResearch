def main(n):
    # Deterministic data generation:
    # chess is a list of 4 "boards", each is a list of n strings, each string length n
    # Characters alternate deterministically based on indices and board index
    chess = []
    chars = ["A", "B", "C", "D"]
    for w in range(4):
        board = []
        for i in range(n):
            row_chars = []
            for j in range(n):
                # Simple deterministic pattern depending on board index and position
                row_chars.append(chars[(w + i + j) % 4])
            board.append("".join(row_chars))
        chess.append(board)

    issue = {0: 0, 1: 0, 2: 0, 3: 0}
    reversed_issue = {0: 0, 1: 0, 2: 0, 3: 0}

    for w in range(4):
        chessdesk = [chess[0] + chess[3]] + [chess[1] + chess[2]]
        for s in range(2 * n):
            chessdesk[0][s] += chessdesk[1][s]
        chessdesk.pop(1)
        chessdesk = chessdesk[0]
        colour = chessdesk[0][0]

        for i in range(2 * n):
            row = chessdesk[i]
            for j in range(2 * n):
                if (i + j) % 2 == 0:
                    if row[j] != colour:
                        issue[w] += 1

                else:
                    if row[j] == colour:
                        issue[w] += 1

        reversed_issue[w] = 4 * n * n - issue[w]
        if w == 0:
            chess[0], chess[3] = chess[3], chess[0]
        elif w == 1:
            chess[1], chess[3] = chess[3], chess[1]
        elif w == 2:
            chess[1], chess[2] = chess[2], chess[1]

    result = min(min(issue.values()), min(reversed_issue.values()))
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(10)