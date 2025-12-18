n = int(input())
chess = []
for w in range(3):
    chess.append([input() for i in range(n)])
    input()
chess.append([input() for i in range(n)])

issue = {0:0, 1:0, 2:0, 3:0}
reversed_issue = {0:0, 1:0, 3:0}

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

    reversed_issue[w] = 4 * n**2 - issue[w]              
    if w == 0:
        chess[0], chess[3] = chess[3], chess[0]
    elif w == 1:
        chess[1], chess[3] = chess[3], chess[1]
    elif w == 2:
        chess[1], chess[2] = chess[2], chess[1]

print(min(min(issue.values()), min(reversed_issue.values())))