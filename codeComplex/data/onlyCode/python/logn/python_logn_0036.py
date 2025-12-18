
l,r = map(int, input().split())

def maxXor(low, high):
    #print(low, high)
    highestPower = high.bit_length()-1
    if high == 1 and low == 0:
        return 1
    if highestPower <= 0:
        return 0
    if low < 2** highestPower:
        return (2**(highestPower+1))-1
    return maxXor(low -2**highestPower, high-2**highestPower)

print(maxXor(l,r))
