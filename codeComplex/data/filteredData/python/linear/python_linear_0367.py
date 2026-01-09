def main(n):
    # Interpret n as the size of both sequences g and b
    games = n
    bills = n

    # Deterministic data generation
    # g is a non-decreasing sequence
    g = [i // 2 for i in range(games)]
    # b is also non-decreasing, with a simple offset pattern
    b = [i // 3 + 1 for i in range(bills)]

    total = 0
    i = 0
    j = 0

    while i < games and j < bills:
        if g[i] <= b[j]:
            total += 1
            i += 1
            j += 1
        elif g[i] > b[j]:
            i += 1

    # print(total)
    pass
if __name__ == "__main__":
    main(10)