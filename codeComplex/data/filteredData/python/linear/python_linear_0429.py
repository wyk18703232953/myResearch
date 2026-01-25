def main(n):
    # n: number of rows (including Thomas as first row)
    # Deterministic data generation: row i has elements [i, i+1, ..., i+(i % 5)]
    S = []
    for i in range(n):
        row = [i + j for j in range((i % 5) + 1)]
        S.append(sum(row))

    if S[0] == max(S):
        print("1")
        return

    thomas = S[0]
    rank = 1
    S.sort(reverse=True)
    for x in S:
        if x == thomas:
            print(rank)
            return
        else:
            rank += 1


if __name__ == "__main__":
    main(10)