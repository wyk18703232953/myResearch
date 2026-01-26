def main(n):
    # Ensure n is at least 1 to avoid degenerate cases
    if n <= 0:
        n = 1

    # Deterministically generate 4*n strings of length n using simple patterns
    base_strings = []
    for idx in range(4 * n):
        # Alternate between 'B' and 'W' in a deterministic pattern depending on idx and position
        s = ''.join('B' if ((idx + j) % 3) else 'W' for j in range(n))
        base_strings.append(s)

    # Build chess as in the original input structure:
    # first three blocks of n strings, with a separator line (ignored) between them in original code
    chess = []
    chess.append(base_strings[0:n])          # first block
    chess.append(base_strings[n:2 * n])      # second block
    chess.append(base_strings[2 * n:3 * n])  # third block
    chess.append(base_strings[3 * n:4 * n])  # fourth block

    issue = {0: 0, 1: 0, 2: 0, 3: 0}
    reversed_issue = {0: 0, 1: 0, 3: 0}

    for w in range(4):
        chessdesk = [chess[0] + chess[3]] + [chess[1] + chess[2]]
        for s in range(2 * n):
            chessdesk[0][s] += chessdesk[1][s]
        chessdesk.pop(1)
        chessdesk = chessdesk[0]
        colour = chessdesk[0][0]

        for i in range(2 * n):
            for j in range(2 * n):
                if (i + j) % 2 == 0:
                    if chessdesk[i][j] != colour:
                        issue[w] += 1

                else:
                    if chessdesk[i][j] == colour:
                        issue[w] += 1

        reversed_issue[w] = 4 * n ** 2 - issue[w]
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
    # Example deterministic run for a chosen scale n
    main(5)