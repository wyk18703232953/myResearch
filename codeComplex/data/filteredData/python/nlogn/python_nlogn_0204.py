def main(n):
    # Deterministic generation of T and tasks
    # Interpret n as the number of tasks
    # Define T proportional to n so that some tasks can be chosen
    T = n * 5

    # Generate n tasks with (index, required_min_count i, duration j)
    # i increases with index, j is a bounded arithmetic function of index
    a = []
    for idx in range(1, n + 1):
        i = (idx % n) + 1  # ensures values in [1, n]
        j = (idx % 7) + 1  # small durations in [1, 8]
        a.append((idx, i, j))

    # Sort by duration (original code sorted by last element)
    a.sort(key=lambda x: x[-1])

    be, en, ans = 0, n, []

    while be < en:
        md, time, c = (be + en + 1) >> 1, 0, 0

        for _, i, j in a:
            if time + j <= T and i >= md:
                time += j
                c += 1

        if c >= md:
            be = md

        else:
            en = md - 1

    l = be
    for _, i, j in a:
        if be and i >= l:
            ans.append(_)
            be -= 1

    # print(f"{l}\n{l}")
    pass

    if ans:
        # print(*ans)
        pass

    else:
        # print()
        pass
if __name__ == "__main__":
    main(10)