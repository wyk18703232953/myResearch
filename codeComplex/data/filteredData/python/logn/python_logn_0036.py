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
    # 根据规模 n 生成测试数据：
    # 生成区间 [l, r]，其中 0 <= l <= r <= 2^n - 1
    if n <= 0:
        l, r = 0, 0
    else:
        max_val = (1 << n) - 1
        l = random.randint(0, max_val)
        r = random.randint(l, max_val)
    result = maxXor(l, r)
    print(result)

if __name__ == "__main__":
    # 示例：可以根据需要调整 n
    main(10)