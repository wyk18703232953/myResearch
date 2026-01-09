def main(n):
    # Interpret n as the number of positions (people), m will be the same as n
    # Generate deterministic dist and taxi arrays
    # dist: strictly increasing positions to respect the original logic that uses ordering
    # taxi: first n//3 as taxis, others as non-taxis (deterministic pattern)
    m = n

    # Generate distances as 1, 2, ..., n
    dist = [i + 1 for i in range(n)]

    # Generate taxi availability: first n//3 are taxis (1), rest are 0
    split = n // 3
    taxi = [1 if i < split else 0 for i in range(n)]

    dists = {}
    d = []
    for person in range(len(taxi)):
        if taxi[person]:
            dists[dist[person]] = 0
            d.append(dist[person])
    start = 0
    d.append(10**11)
    for person in range(len(taxi)):
        if taxi[person] == 0:
            while dist[person] > d[start + 1]:
                start += 1
            if abs(dist[person] - d[start]) <= abs(dist[person] - d[start + 1]):
                dists[d[start]] += 1

            else:
                dists[d[start + 1]] += 1
    out = []
    for key in dists:
        if key != 10**11:
            out.append(str(dists[key]))

        else:
            out.append('')
    # print(' '.join(out))
    pass
if __name__ == "__main__":
    main(10)