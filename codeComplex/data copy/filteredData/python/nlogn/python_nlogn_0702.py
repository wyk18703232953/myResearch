def main(n):
    # Generate deterministic input data based on n
    # Interpret n as length of array a
    # Construct a sequence with some pattern that can exercise logic
    a = [(i // 2) for i in range(n)]

    d = set()
    t = {}
    rep = set()

    # Core logic unchanged, except input/output removed
    if a.count(0) >= 2:
        return "cslnb"

    for i in a:
        if i in d:
            if t[i] + 1 == 3:
                return "cslnb"

            else:
                t[i] += 1
                rep.add(i)
                if len(rep) >= 2:
                    return "cslnb"

        else:
            t[i] = 1
            d.add(i)

    if rep:
        for c in rep:
            if c - 1 in d:
                return "cslnb"

    s = 0
    a.sort()
    for i in range(n):
        s += a[i] - i

    if s % 2 == 1:
        return "sjfnb"

    else:
        return "cslnb"


if __name__ == "__main__":
    # Example deterministic calls for experimentation
    for size in [1, 2, 5, 10, 20]:
        result = main(size)
        # print(size, result)
        pass