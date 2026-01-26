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
    if n < 1:
        n = 1
    l = 0
    r = n
    result = maxXor(l, r)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)