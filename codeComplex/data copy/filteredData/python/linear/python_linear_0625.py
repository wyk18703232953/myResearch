def main(n):
    # Interpret n as the number of positions (people), with at least 2
    n = max(2, int(n))

    # Deterministic generation of distances: strictly increasing
    # Example: dist[i] = (i + 1) * 10
    dist = [(i + 1) * 10 for i in range(n)]

    # Deterministic generation of taxi availability pattern
    # Example pattern:
    # - Index 0 is always a taxi
    # - For i > 0, taxi[i] = 1 if (i % 3 == 0) else 0
    taxi = [0] * n
    for i in range(n):
        if i == 0 or i % 3 == 0:
            taxi[i] = 1

    # Core logic preserved from original program
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
    for key in dists:
        # print(dists[key] if key != 10**11 else "", end=" ")
        pass
    # print()
    pass
if __name__ == "__main__":
    main(10)