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

    max_val = max(table)
    ind = 0
    while ind < len(table):
        if table[ind] == max_val:
            break
        ind += 1
    if ind == 0:
        cost = len(table)
    else:
        cost = (len(table) - ind) + table[ind - 1]

    options = []
    for i in range(n):
        if i == 0:
            cost = n
        else:
            cost = (n - i) + table[i - 1]
        options.append(cost)
    min_cost = min(options)

    return min(table[n - 1], min_cost)

def generate_beacons(n):
    # Deterministic generation: positions strictly increasing, powers vary with simple arithmetic
    beacons = []
    for i in range(n):
        position = i * 3 + (i // 2)
        power = (i % 5) + (i // 3)
        beacons.append((position, power))
    beacons.sort()
    return beacons

def main(n):
    beacons = generate_beacons(n)
    result = chain_reaction(n, beacons)
    print(result)

if __name__ == "__main__":
    main(10)