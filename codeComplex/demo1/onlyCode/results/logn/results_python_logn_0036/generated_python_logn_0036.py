import random

def maxXor(low, high):
    highestPower = high.bit_length() - 1
    if high == 1 and low == 0:
        return 1
    if highestPower <= 0:
        return 0
    if low < 2 ** highestPower:
        return (2 ** (highestPower + 1)) - 1
    return maxXor(low - 2 ** highestPower, high - 2 ** highestPower)

def main(n):
    # 生成测试数据：
    # 1. 确保范围在 [0, n]
    # 2. 随机生成 l, r 且 l <= r
    if n < 1:
        l, r = 0, 0
    else:
        l = random.randint(0, n)
        r = random.randint(l, n)
    print(maxXor(l, r))

if __name__ == "__main__":
    # 示例：可修改为任何需要的规模 n
    main(100)