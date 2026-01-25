import sys

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
            mid = int(lo + (hi - lo) / 2)
            if beacons[mid][0] < r:
                lo = mid + 1
            else:
                hi = mid - 1
        destroyed += table[hi] if hi >= 0 else 0
        destroyed += (i - (hi + 1))
        table[i] = destroyed

    cost = n
    ind = 0
    while ind < len(table):
        cost = min(cost, n - ind - 1 + table[ind])
        ind += 1
    return cost

def generate_beacons(n):
    beacons = []
    for i in range(n):
        position = i * 2 + 1
        power = (i * 3) % (n + 1)
        beacons.append((position, power))
    beacons.sort()
    return beacons

def main(n):
    beacons = generate_beacons(n)
    result = chain_reaction(n, beacons)
    print(result)

if __name__ == "__main__":
    main(10)