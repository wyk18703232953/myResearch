def main(n):
    # Interpret n as the size of both lists
    games = n
    bills = n

    # Deterministic data generation
    # g: 1, 2, 3, ..., n
    # b: 2, 3, 4, ..., n+1
    g = [i + 1 for i in range(games)]
    b = [i + 2 for i in range(bills)]

    total = 0
    i = 0
    j = 0

    # Core algorithm logic preserved
    while i < games and j < bills:
        if g[i] <= b[j]:
            total += 1
            i += 1
            j += 1
        elif g[i] > b[j]:
            i += 1

    print(total)


if __name__ == "__main__":
    # Example call for experimental purposes
    main(10)