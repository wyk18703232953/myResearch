def main(n):
    # n controls the number of test cases
    # For each test case we deterministically generate 3 tile strings.
    # Each tile is of form "<digit><suit>", digit in 1..9, suit in {"m","p","s"}.
    # We then apply the original algorithm to each test case and print the result.

    def generate_tile(k):
        # k is a non-negative integer, map it deterministically to a tile
        digit = (k % 9) + 1
        suit = "mps"[k % 3]
        return str(digit) + suit

    def solve_one(m):
        # m is a list of 3 tile strings, replicate original logic

        tiles = [[0 for _ in range(9)] for _ in range(3)]
        for i in range(len(m)):
            g = int(m[i][0]) - 1
            h = m[i][1]
            if h == "m":
                tiles[0][g] += 1
            elif h == "p":
                tiles[1][g] += 1
            else:
                tiles[2][g] += 1

        if m[0] == m[1] and m[1] == m[2]:
            print(0)
        elif m[0] == m[1]:
            print(1)
        elif m[0] == m[2]:
            print(1)
        elif m[1] == m[2]:
            print(1)
        else:
            flag = False
            for i in range(3):
                for j in range(9):
                    if tiles[i][j] != 0:
                        if j != 8 and tiles[i][j + 1] != 0:
                            if j != 7 and tiles[i][j + 2] != 0:
                                print(0)
                                flag = True
                                break
                            else:
                                print(1)
                                flag = True
                                break
                        elif j != 7 and j != 8 and tiles[i][j + 2] != 0:
                            print(1)
                            flag = True
                            break
                if flag:
                    break
            if flag is False:
                print(2)

    if n <= 0:
        return

    for t in range(n):
        base = t * 3
        m = [generate_tile(base + i) for i in range(3)]
        solve_one(m)


if __name__ == "__main__":
    # Example: run main with a specific scale
    main(10)