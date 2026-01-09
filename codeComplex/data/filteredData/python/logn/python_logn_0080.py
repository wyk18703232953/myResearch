def main(n):
    # Interpret n as the upper bound r, with l fixed to 0
    l = 0
    r = n
    xor_val = l ^ r

    bms = 0
    while xor_val != 0:
        bms = bms + 1
        xor_val = xor_val >> 1

    maxxor = 0
    dois = 1
    while bms != 0:
        maxxor = maxxor + dois
        dois = dois << 1
        bms = bms - 1

    # print(maxxor)
    pass
if __name__ == "__main__":
    main(10)