def main(n):
    # n: number of time points
    # Deterministically generate s and the list of times a
    # s grows with n but stays relatively small compared to minutes in a day
    s = (n * 3 + 7) % 100 + 1  # ensure s in [1,100]

    a = []
    # generate n times in minutes, strictly increasing, within a day
    # base increment pattern depends on index to avoid trivial uniformity
    current = 0
    for i in range(n):
        inc = (i * 5 + 13) % 60 + 1  # increment between 1 and 60 minutes
        current += inc
        # wrap within 0..1439 but keep increasing sequence by adding days if needed
        # not strictly necessary for logic, but keeps values in a reasonable range
        a.append(current % (24 * 60))

    # sort to mimic typical input order and guarantee non-decreasing
    a.sort()

    if n == 0:
        # Edge case: no events, mimic original logic:
        # a[0] would not exist, so just print earliest possible time
        # print(0, 0)
        pass
        return

    if a[0] != 0 and a[0] > s:
        # print(0, 0)
        pass

    else:
        a.append(a[n - 1] + 2 * s + 3)
        for i in range(1, n + 1):
            if a[i] - (a[i - 1] + 2 + s) >= s:
                t = a[i - 1] + s + 1
                # print(t // 60, t % 60)
                pass
                break


if __name__ == "__main__":
    # example call for experimentation; adjust n as needed
    main(10)