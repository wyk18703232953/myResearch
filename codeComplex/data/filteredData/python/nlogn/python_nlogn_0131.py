def main(n):
    # Interpret n as:
    # f = n  (number of filters)
    # d = 2*n (required sockets)
    # s = 1  (initial free sockets)
    f = n
    d = 2 * n
    s = 1

    # Deterministic generation of filters: simple increasing sequence
    filters = [i % 5 + 2 for i in range(1, f + 1)]
    filters.sort(reverse=True)

    freeSockets = s
    usedFilters = 0
    for i in range(len(filters)):
        if freeSockets >= d:
            break
        usedFilters += 1
        freeSockets += filters[i] - 1

    if freeSockets >= d:
        # print(usedFilters)
        pass

    else:
        # print(-1)
        pass
if __name__ == "__main__":
    main(10)