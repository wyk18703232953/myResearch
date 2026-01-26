import math

def maxXor(l, r):
    if l == r:
        return 0
    xor = l ^ r
    twoPows = math.log(xor, 2)
    return 2 ** int(math.floor(twoPows) + 1) - 1

def main(n):
    l = n
    r = 2 * n + 1
    result = maxXor(l, r)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)