import math

def main(n):
    if n <= 0:
        return 0

    # 确定性生成 n 个 (a, b) 对
    # a 为严格递增的正整数，b 为与 a 相关的确定性值
    beacons = {}
    sortedKeys = [0] * n
    for i in range(n):
        a = i + 1
        b = (a // 2) + (a % 3)
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

    return minF

if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 规模
    result = main(10)
    print(result)