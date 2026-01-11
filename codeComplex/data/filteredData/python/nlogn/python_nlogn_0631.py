def main(n):
    # Interpret n as m, the total number of positions
    m = max(1, n)

    # Deterministic data generation:
    # distances: [0, 1, 2, ..., m-1]
    distances = list(range(m))
    # taxiDriver: pattern 0,1,0,1,... to ensure both people and drivers exist
    taxiDriver = [i % 2 for i in range(m)]

    people = []
    drivers = []
    result = [0] * m

    for i in range(len(distances)):
        if taxiDriver[i]:
            drivers.append(distances[i])

        else:
            people.append(distances[i])

    if not drivers:
        # Edge case: no drivers, just return zeros
        # print(' '.join(map(str, result)))
        pass
        return

    j = 0
    for person in people:
        if (j + 1) < len(drivers):
            while (j + 1) < len(drivers) and (drivers[j] - person) < (person - drivers[j + 1]):
                j += 1
            result[j] += 1

        else:
            result[j] += 1

    # print(' '.join(map(str, result)))
    pass
if __name__ == "__main__":
    main(10)