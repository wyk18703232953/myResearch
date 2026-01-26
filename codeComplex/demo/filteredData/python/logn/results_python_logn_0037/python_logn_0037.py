import math

def maxor(bawah, atas):
    if bawah == atas:
        return 0
    xor = bawah ^ atas
    pangkat2 = math.log(xor, 2)
    return 2 ** int(math.floor(pangkat2) + 1) - 1

def main(n):
    bawah = n
    atas = 2 * n + 1
    result = maxor(bawah, atas)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)