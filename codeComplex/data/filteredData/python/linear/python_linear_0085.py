def chain_reaction(n, beacons):
    table = [0] * n
    for i in range(n):
        position = beacons[i][0]
        power = beacons[i][1]
        destroyed = 0
        r = position - power
        lo = 0
        hi = len(beacons) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if beacons[mid][0] < r:
                lo = mid + 1

            else:
                hi = mid - 1
        destroyed += table[hi] if hi >= 0 else 0
        destroyed += (i - (hi + 1))
        table[i] = destroyed

    options = []
    for i in range(n):
        prev = table[i - 1] if i - 1 >= 0 else 0
        cost = (n - i) + prev
        options.append(cost)
    min_cost = min(options)
    return min(table[n - 1], min_cost)


def generate_beacons(n):
    beacons = []
    for i in range(n):
        position = i * 3 + 1
        power = (i * 2 + 1) % (n + 1)
        beacons.append((position, power))
    beacons.sort()
    return beacons


def main(n):
    beacons = generate_beacons(n)
    result = chain_reaction(n, beacons)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)