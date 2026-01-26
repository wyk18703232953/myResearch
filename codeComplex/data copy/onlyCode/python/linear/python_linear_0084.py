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
        destroyed += table[hi]
        # beacons destroyed by currently activated one
        destroyed += (i - (hi + 1))
        table[i] = destroyed

    # print(table)

    # find first index of max # of beacons destroyed
    max_val = max(table)
    ind = 0
    while ind < len(table):
        if table[ind] == max_val:
            break
        ind += 1
    cost = (len(table) - ind) + table[ind - 1]

    options = []
    for i in range(n):
        cost = (n - i) + table[i - 1]
        options.append(cost)
    min_cost = min(options)

    # options: add a beacon that doesn't destroy any or add a beacon that destroys the beacon at index ind
    # return min(table[n - 1], cost)
    return min(table[n - 1], min_cost)
 
n = int(sys.stdin.readline().strip())
beacons = []
for i in range(n):
    a, b = [int(x) for x in sys.stdin.readline().strip().split(" ")]
    beacons.append((a, b))
beacons.sort()
print(chain_reaction(n, beacons))