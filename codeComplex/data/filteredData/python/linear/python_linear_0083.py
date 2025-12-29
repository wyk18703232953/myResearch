import random

def chain_reaction(n, beacons):
    table = [0] * n
    # table[i] represents the number of beacons destroyed if the first i beacons are used
    for i in range(n):
        position = beacons[i][0]
        power = beacons[i][1]
        destroyed = 0
        r = position - power
        # use binary search to find the beacon that will be activated after the current one
        lo = 0
        hi = len(beacons) - 1
        while lo <= hi:
            mid = int(lo + (hi - lo) / 2)
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

    # find first index of max # of beacons destroyed
    cost = n
    ind = 0
    while ind < len(table):
        cost = min(cost, n - ind - 1 + table[ind])
        ind += 1

    # options: add a beacon that doesn't destroy any or add a beacon that destroys the beacon at index ind
    return cost


def generate_test_data(n):
    # 生成 n 个信标 (position, power)
    # 假设位置在 [0, 10*n]，功率在 [0, 5*n]
    beacons = []
    for _ in range(n):
        pos = random.randint(0, 10 * n)
        power = random.randint(0, 5 * n)
        beacons.append((pos, power))
    beacons.sort()
    return beacons


def main(n):
    beacons = generate_test_data(n)
    result = chain_reaction(n, beacons)
    print(result)


if __name__ == "__main__":
    # 示例：可在此处修改 n 的值进行快速测试
    main(5)