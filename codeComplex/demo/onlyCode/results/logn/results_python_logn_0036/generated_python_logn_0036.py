def main(n):
    l = 0
    r = n

    def maxXor(low, high):
        highestPower = high.bit_length() - 1
        if high == 1 and low == 0:
            return 1
        if highestPower <= 0:
            return 0
        if low < 2 ** highestPower:
            return (2 ** (highestPower + 1)) - 1
        return maxXor(low - 2 ** highestPower, high - 2 ** highestPower)

    return maxXor(l, r)


if __name__ == "__main__":
    print(main(10))