def main(n):
    # Deterministic generation of board of size n with positive integers
    # Ensure values in [1, n]; avoid zeros because original logic assumes moves
    if n <= 0:
        return
    board = [(i % n) + 1 for i in range(n)]

    index = list(range(0, n))
    ascending = [x for _, x in sorted(zip(board, index))]

    winners = n * [""]

    for c in reversed(ascending):
        if board[c] == n:
            winners[c] = "B"
        toCheck = c - board[c]
        while toCheck >= 0:
            if winners[toCheck] == "B":
                winners[c] = "A"
            toCheck = toCheck - board[c]
        if winners[c] == "":
            toCheck = c + board[c]
            while toCheck < n:
                if winners[toCheck] == "B":
                    winners[c] = "A"
                toCheck = toCheck + board[c]
        if winners[c] == "":
            winners[c] = "B"

    for i in range(n):
        print(winners[i], end="")
    print()


if __name__ == "__main__":
    main(10)