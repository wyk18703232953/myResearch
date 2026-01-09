def main(n):
    # n controls how many different 3-tile hands we test; we cycle deterministically over a fixed tile universe
    # Tile format in original problem: digit(1-9) + suit('m','p','s')
    digits = [str((i % 9) + 1) for i in range(9)]
    suits = ['m', 'p', 's']
    universe = [d + s for d in digits for s in suits]  # 27 distinct tiles

    results = []
    for k in range(max(1, n)):
        # Generate a deterministic 3-tile hand from k
        t1 = universe[k % 27]
        t2 = universe[(k // 3) % 27]
        t3 = universe[(k // 9) % 27]
        m = [t1, t2, t3]

        tiles = [[0 for _ in range(9)] for _ in range(3)]
        for x in m:
            g = int(x[0]) - 1
            h = x[1]
            if h == "m":
                tiles[0][g] += 1
            elif h == "p":
                tiles[1][g] += 1

            else:
                tiles[2][g] += 1

        if m[0] == m[1] and m[1] == m[2]:
            res = 0
        elif m[0] == m[1]:
            res = 1
        elif m[0] == m[2]:
            res = 1
        elif m[1] == m[2]:
            res = 1

        else:
            found = False
            for i in range(3):
                for j in range(9):
                    if tiles[i][j] != 0:
                        if j != 8 and tiles[i][j + 1] != 0:
                            if j != 7 and tiles[i][j + 2] != 0:
                                res = 0
                                found = True
                                break

                            else:
                                res = 1
                                found = True
                                break
                        elif j != 7 and j != 8 and tiles[i][j + 2] != 0:
                            res = 1
                            found = True
                            break
                if found:
                    break
            if not found:
                res = 2
        results.append(res)

    # To keep comparable output size, aggregate results deterministically
    # Print the sum and last value so runtime isn't optimized away
    # print(sum(results), results[-1])
    pass
if __name__ == "__main__":
    main(1000)