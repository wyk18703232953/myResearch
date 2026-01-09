def main(n):
    # Generate deterministic test data of size n
    # Tiles are from "1s".."9s", "1m".."9m", "1p".."9p"
    suits = ["s", "m", "p"]
    tiles = []
    for i in range(n):
        num = (i % 9) + 1
        suit = suits[(i // 9) % 3]
        tiles.append(str(num) + suit)

    # Core algorithm (unchanged logic, no input())
    m = {"s": [0] * 9, "m": [0] * 9, "p": [0] * 9}
    for e in tiles:
        m[e[1]][int(e[0]) - 1] += 1
    ret = 2
    for t in "smp":
        l = m[t]
        if max(l) >= 2:
            ret = min(ret, 3 - max(l))

        else:
            for i in range(7):
                seq = sum(l[i:i + 3])
                ret = min(ret, 3 - seq)
    # print(ret)
    pass
if __name__ == "__main__":
    main(14)