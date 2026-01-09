def main(n):
    # Generate deterministic data based on n
    t = n
    last = []
    current = []

    # Generate last list: strings "a0", "a1", ..., "a(t-1)"
    for i in range(t):
        last.append("a" + str(i))

    # Generate current list as a shifted version of last, with some overlaps
    # current[i] = last[(i*2) % t] ensures deterministic pattern and duplicates
    for i in range(t):
        current.append("a" + str((i * 2) % t))

    # Core logic from original program
    for i in range(len(last)):
        if last[i] in current:
            current[current.index(last[i])] = "*"
            last[i] = "*"

    last.sort()
    current.sort()

    total = 0
    for i in range(len(last)):
        if last[i] == current[i]:
            continue

        else:
            total += 1

    # print(total)
    pass
if __name__ == "__main__":
    # Example call; adjust n as needed for experiments
    main(10)