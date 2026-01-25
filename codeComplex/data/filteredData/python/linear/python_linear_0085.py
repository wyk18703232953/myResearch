import sys

def chain_reaction(n, beacons):
    table = [0] * n
    # table[i] represents the number of beacons destroyed if the first i beacons are used
    for i in range(n):
        position = beacons[i][0]
        power = beacons[i][1]
        destroyed = 0
        r = position - power
        b = 0
        # use binary search to find the beacon that will be activated after the current one
        lo = 0
        hi = len(beacons) - 1
        while lo <= hi:
            mid = int(lo + (hi - lo) / 2)
            pos = beacons[mid][0]
            if beacons[mid][0] < r:
                lo = mid + 1
            else:
                hi = mid - 1
        # beacons destroyed by next activated one
        if hi >= 0:
            destroyed += table[hi]
        # beacons destroyed by currently activated one
        destroyed += (i - (hi + 1))
        table[i] = destroyed

    # calculate cost of placing a beacon that activates each beacon in the table
    options = []
    for i in range(n):
        if i == 0:
            cost = (n - i)
        else:
            cost = (n - i) + table[i - 1]
        options.append(cost)
    min_cost = min(options)

    # options: add a beacon that doesn't destroy any or add a beacon that destroys the beacon with minimum cost
    return min(table[n - 1], min_cost)

def generate_beacons(n):
    # deterministic generation: positions strictly increasing, powers vary with simple arithmetic
    beacons = []
    for i in range(n):
        position = 2 * i + 1
        power = (i * 3) // 2 + 1
        beacons.append((position, power))
    beacons.sort()
    return beacons

def main(n):
    beacons = generate_beacons(n)
    result = chain_reaction(n, beacons)
    print(result)

if __name__ == "__main__":
    main(10)