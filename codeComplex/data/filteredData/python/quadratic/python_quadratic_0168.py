def main(n):
    # Interpret n as the length of the list l
    # Deterministically generate k and l based on n
    # Ensure k is in a reasonable range, e.g., 1 to 20
    k = (n % 20) + 1
    # Generate l with values in range [0, 255] deterministically
    l = [(i * 7 + 13) % 256 for i in range(n)]

    maps = []
    for _ in range(256):
        maps.append(['empty', 0])
    output = []
    for innum in l:
        if maps[innum][0] == 'chosen':
            outnum = maps[innum][1]
        elif maps[innum][0] == 'potential':
            outnum = maps[innum][1]
            i = innum
            while i >= 0 and maps[i][0] == 'potential':
                maps[i] = ['chosen', outnum]
                i -= 1

        else:
            i = innum
            while i >= 0 and i >= innum - (k - 1) and maps[i][0] != 'chosen':
                i -= 1
            i += 1
            outnum = i
            for j in range(outnum, innum + 1):
                maps[j] = ['chosen', outnum]
            if innum < 255:
                for j in range(innum + 1, min(256, outnum + k)):
                    if maps[j][0] != 'chosen':
                        maps[j] = ['potential', outnum]
        output.append(str(outnum))
    # print(' '.join(output))
    pass
if __name__ == "__main__":
    # Example deterministic call for testing and timing
    main(1000)