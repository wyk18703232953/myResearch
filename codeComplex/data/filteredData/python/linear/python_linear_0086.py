import math

def main(n):
    if n <= 0:
        # print(0)
        pass
        return

    # Deterministic data generation:
    # Generate n beacons with positions strictly increasing
    # a_i = i+1, b_i = (i % max(1, n//3)) + 1 to keep radii bounded but scalable
    beacons = {}
    sortedKeys = [0] * n
    radius_base = max(1, n // 3)
    for i in range(n):
        a = i + 1
        b = (i % radius_base) + 1
        sortedKeys[i] = a
        beacons[a] = b

    sortedKeys.sort()
    maxA = sortedKeys[-1]

    sumBeacons = [0] * (maxA + 1)
    count = 0
    for a in range(maxA + 1):
        sumBeacons[a] = count
        if a in beacons:
            count += 1

    f = [0] * (n + 1)
    minF = math.inf
    for i in range(1, n + 1):
        a = sortedKeys[i - 1]
        b = beacons[a]
        end = max(0, a - b)
        numDestroyed = sumBeacons[a] - sumBeacons[end]
        f[i] = numDestroyed
        if i - numDestroyed > 0:
            f[i] += f[(i - 1) - numDestroyed]
        minF = min(minF, f[i] + n - i)

    # print(minF)
    pass
if __name__ == "__main__":
    main(10)