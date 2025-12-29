import math
import random

def main(n: int) -> int:
    # 1. 生成测试数据：n 个灯塔 (a, b)
    #   假设 a 为正整数且互不相同，b 为非负整数，且不超过 a
    #   这样 a-b >= 0，避免越界问题
    coords = set()
    while len(coords) < n:
        coords.add(random.randint(0, 5 * n))  # 控制范围，避免 maxA 过大
    sortedA = sorted(coords)
    beacons = {}
    for a in sortedA:
        b = random.randint(0, a)  # 确保 a-b >= 0
        beacons[a] = b

    # 原逻辑开始
    sortedKeys = sortedA[:]  # 已经是排序后的 a
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

    # 输出结果
    print(minF)
    return minF


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)